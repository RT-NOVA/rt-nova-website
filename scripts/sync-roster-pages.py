#!/usr/bin/env python3
"""
Generate lightweight Hugo roster route pages from season roster data.

Source of truth:
  data/seasons/<season_id>/rosters/<roster_key>.yaml

Generated route:
  content/rosters/<season_id>-<roster_key>.md

This script intentionally uses only the Python standard library. It only needs
top-level scalar fields from each roster YAML file; Hugo reads the full YAML
data when it renders the page.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


GENERATED_BY = "scripts/sync-roster-pages.py"
GENERATED_MARKER = "generated_by: sync-roster-pages"
START_MARKER = "<!-- BEGIN GENERATED ROSTER ROUTE -->"
END_MARKER = "<!-- END GENERATED ROSTER ROUTE -->"


def repo_root_from(start: Path) -> Path:
    current = start.resolve()
    for path in [current, *current.parents]:
        if (path / "data").is_dir() and (path / "content").is_dir():
            return path
    raise SystemExit(
        "Could not find repo root. Run from the Hugo repo root, or pass --repo-root."
    )


def strip_yaml_quotes(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if (value[0] == value[-1]) and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_top_level_scalars(path: Path) -> Dict[str, str]:
    """
    Parse simple top-level YAML scalar fields.

    This deliberately stops reading once list/detail sections begin, because we
    only need page metadata such as team, season, summary, and date.
    """
    scalars: Dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        # Stop at nested/list detail sections.
        if line.startswith("players:") or line.startswith("staff:"):
            break

        if raw_line[:1].isspace():
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue

        key, value = match.groups()
        value = value.strip()

        # Skip block/list/object values. They are not needed for route stubs.
        if value in {"", "|", ">"} or value.startswith("[") or value.startswith("{"):
            continue

        scalars[key] = strip_yaml_quotes(value)

    return scalars


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def title_from(season_id: str, roster_key: str, scalars: Dict[str, str]) -> str:
    if scalars.get("page_title"):
        return scalars["page_title"]

    team = scalars.get("team") or roster_key.replace("-", " ").upper()
    return f"{season_id} {team} Roster"


def summary_from(scalars: Dict[str, str], title: str) -> str:
    return scalars.get("summary") or f"{title}."


def date_from(existing_path: Path, scalars: Dict[str, str]) -> str:
    if scalars.get("page_date"):
        return scalars["page_date"]

    if existing_path.exists():
        for line in existing_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("date:"):
                return strip_yaml_quotes(line.split(":", 1)[1].strip())

    return "2026-06-16"


def roster_data_files(repo: Path) -> Iterable[Tuple[str, str, Path]]:
    seasons_root = repo / "data" / "seasons"
    if not seasons_root.is_dir():
        return []

    results: List[Tuple[str, str, Path]] = []
    for season_dir in sorted(seasons_root.iterdir()):
        if not season_dir.is_dir():
            continue
        roster_dir = season_dir / "rosters"
        if not roster_dir.is_dir():
            continue

        for path in sorted(roster_dir.glob("*.y*ml")):
            if path.name.startswith("."):
                continue
            results.append((season_dir.name, path.stem, path))

    return results


def route_slug_from(season_id: str, roster_key: str, scalars: Dict[str, str]) -> str:
    """
    Return the generated content filename stem.

    By default, a roster data file like:
      data/seasons/2026/rosters/13u-orange.yaml

    generates:
      content/rosters/2026-13u-orange.md

    Use route_slug when the public URL should differ from the data key, such as
    keeping a spring page at /rosters/2026-11u/ while storing the source data in
    11u-spring.yaml.
    """
    return scalars.get("route_slug") or f"{season_id}-{roster_key}"


def render_route_page(season_id: str, roster_key: str, data_path: Path, existing_path: Path) -> str:
    scalars = parse_top_level_scalars(data_path)
    route_slug = route_slug_from(season_id, roster_key, scalars)
    title = title_from(season_id, roster_key, scalars)
    summary = summary_from(scalars, title)
    date = date_from(existing_path, scalars)

    front_matter = [
        "---",
        f"title: {yaml_string(title)}",
        f"date: {yaml_string(date)}",
        f"season_id: {yaml_string(season_id)}",
        f"roster_key: {yaml_string(roster_key)}",
        f"route_slug: {yaml_string(route_slug)}",
        f"summary: {yaml_string(summary)}",
        GENERATED_MARKER,
        "---",
    ]

    body = [
        START_MARKER,
        f"This file is generated by `{GENERATED_BY}`.",
        "",
        "Do not edit this markdown file directly.",
        f"Edit `data/seasons/{season_id}/rosters/{roster_key}.yaml` and run:",
        "",
        "```bash",
        f"python3 {GENERATED_BY}",
        "```",
        END_MARKER,
        "",
    ]

    return "\n".join(front_matter + body)


def sync(repo: Path, check: bool = False, prune: bool = True) -> int:
    content_dir = repo / "content" / "rosters"
    content_dir.mkdir(parents=True, exist_ok=True)

    generated_paths: List[Path] = []
    changes: List[str] = []

    for season_id, roster_key, data_path in roster_data_files(repo):
        scalars = parse_top_level_scalars(data_path)
        route_slug = route_slug_from(season_id, roster_key, scalars)
        out_path = content_dir / f"{route_slug}.md"
        generated_paths.append(out_path)

        desired = render_route_page(season_id, roster_key, data_path, out_path)
        current = out_path.read_text(encoding="utf-8") if out_path.exists() else None

        if current != desired:
            changes.append(f"update {out_path.relative_to(repo)}")
            if not check:
                out_path.write_text(desired, encoding="utf-8")

    if prune:
        generated_set = {path.resolve() for path in generated_paths}
        for path in sorted(content_dir.glob("*.md")):
            if path.resolve() in generated_set:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if GENERATED_MARKER in text or START_MARKER in text:
                changes.append(f"delete {path.relative_to(repo)}")
                if not check:
                    path.unlink()

    if changes:
        print("Roster route sync changes:")
        for change in changes:
            print(f" - {change}")
        if check:
            print("\nRoute files are not in sync.")
            return 1
    else:
        print("Roster route pages are already in sync.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate content/rosters/*.md route stubs from data/seasons/*/rosters/*.yaml."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Path to the Hugo repo root. Defaults to auto-detecting from the current directory.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether generated route files are up to date without writing changes.",
    )
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help="Do not delete stale generated roster route files.",
    )
    args = parser.parse_args()

    repo = args.repo_root.resolve() if args.repo_root else repo_root_from(Path.cwd())
    return sync(repo, check=args.check, prune=not args.no_prune)


if __name__ == "__main__":
    sys.exit(main())
