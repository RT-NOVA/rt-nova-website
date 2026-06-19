#!/usr/bin/env python3
"""
Social Hub Image Sync

Downloads remote Social Hub images once and stores them locally under
static/images/social/ so Hugo never depends on Facebook/Instagram CDN
hotlinks at render time.

Usage examples:

  python3 scripts/social-hub-image-sync.py --dry-run
  python3 scripts/social-hub-image-sync.py
  python3 scripts/social-hub-image-sync.py --force
  python3 scripts/social-hub-image-sync.py --post content/social-hub/2026-facebook-11u-photo-example.md

Front matter behavior:

- If source_image_url exists, that URL is used as the download source.
- Else, if image is an http(s) URL, that URL is moved into source_image_url and used.
- If image is already a local non-placeholder path, the post is skipped unless --force is used.
- If image is a known platform placeholder and source_image_url exists, the utility replaces it
  with the downloaded local image.
"""

from __future__ import annotations

import argparse
import mimetypes
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

ROOT = Path(".")
DEFAULT_CONTENT_DIRS = [Path("content/social-hub")]
OUTPUT_DIR = Path("static/images/social")

KNOWN_PLACEHOLDER_IMAGES = {
    "/images/social/facebook-program-update.svg",
    "/images/social/instagram-team-moments.svg",
    "/images/social/static-program-note.svg",
}

IMAGE_EXT_BY_CONTENT_TYPE = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
}

REMOTE_PREFIXES = ("http://", "https://")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download Social Hub post images to local static assets.")
    parser.add_argument("--content-dir", action="append", default=[], help="Content directory to scan. Can be used more than once.")
    parser.add_argument("--post", action="append", default=[], help="Specific markdown post to process. Can be used more than once.")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Output directory for downloaded images.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without downloading or writing files.")
    parser.add_argument("--force", action="store_true", help="Re-download even if the post already has a local image.")
    parser.add_argument("--timeout", type=int, default=30, help="Download timeout in seconds.")
    parser.add_argument("--clear-failed-remote", action="store_true", help="If a remote image fails to download, remove it from image: so the site shows the placeholder instead of a broken hotlink.")
    return parser.parse_args()


def read_front_matter(path: Path) -> Tuple[str, str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated YAML front matter")
    front = text[4:end]
    rest = text[end + len("\n---") :]
    return text[:4], front, rest


def parse_scalar_fields(front: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    for line in front.splitlines():
        if not line or line.startswith(" ") or line.startswith("-"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)\s*$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        fields[key] = value
    return fields


def quote_yaml(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def set_field(front: str, key: str, value: str, *, before_key: Optional[str] = None) -> str:
    replacement = f"{key}: {quote_yaml(value)}"
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", re.MULTILINE)
    if pattern.search(front):
        return pattern.sub(replacement, front, count=1)

    if before_key:
        before_pattern = re.compile(rf"^{re.escape(before_key)}:\s*.*$", re.MULTILINE)
        match = before_pattern.search(front)
        if match:
            return front[: match.start()] + replacement + "\n" + front[match.start() :]

    return front.rstrip() + "\n" + replacement + "\n"


def remove_field(front: str, key: str) -> str:
    return re.sub(rf"^{re.escape(key)}:\s*.*\n?", "", front, count=1, flags=re.MULTILINE)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "social-post"


def is_remote(value: str) -> bool:
    return value.startswith(REMOTE_PREFIXES)


def is_known_placeholder(value: str) -> bool:
    return value in KNOWN_PLACEHOLDER_IMAGES


def determine_ext(url: str, content_type: Optional[str]) -> str:
    if content_type:
        ctype = content_type.split(";")[0].strip().lower()
        if ctype in IMAGE_EXT_BY_CONTENT_TYPE:
            return IMAGE_EXT_BY_CONTENT_TYPE[ctype]

    parsed = urllib.parse.urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}:
        return ".jpg" if suffix == ".jpeg" else suffix

    guessed, _ = mimetypes.guess_type(parsed.path)
    if guessed in IMAGE_EXT_BY_CONTENT_TYPE:
        return IMAGE_EXT_BY_CONTENT_TYPE[guessed]

    return ".jpg"


def date_prefix(fields: Dict[str, str], path: Path) -> str:
    date = fields.get("date", "")
    match = re.match(r"^(\d{4}-\d{2}-\d{2})", date)
    if match:
        return match.group(1)

    name_match = re.match(r"^(\d{4}-\d{2}-\d{2})", path.stem)
    if name_match:
        return name_match.group(1)

    return "undated"


def output_name(path: Path, fields: Dict[str, str], ext: str) -> str:
    platform = fields.get("platform", fields.get("source_type", "social"))
    title = fields.get("title", path.stem)
    prefix = date_prefix(fields, path)
    return f"{prefix}-{slugify(platform)}-{slugify(title)}{ext}"


def download_image(url: str, timeout: int) -> Tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; RT-NOVA-SocialHubImageSync/1.0)",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        },
    )

    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        data = response.read()

    if content_type and not content_type.lower().startswith("image/"):
        # Some CDNs omit or mangle content-type, so allow common image signatures.
        if not (
            data.startswith(b"\xff\xd8\xff")
            or data.startswith(b"\x89PNG")
            or data.startswith(b"GIF8")
            or data.startswith(b"RIFF")
            or data.lstrip().startswith(b"<svg")
        ):
            raise ValueError(f"download did not return an image content type: {content_type}")

    if len(data) < 100:
        raise ValueError("downloaded image is unexpectedly small")

    return data, content_type


def iter_posts(args: argparse.Namespace) -> Iterable[Path]:
    if args.post:
        for item in args.post:
            yield Path(item)
        return

    dirs = [Path(p) for p in args.content_dir] if args.content_dir else DEFAULT_CONTENT_DIRS
    for directory in dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "_index.md":
                continue
            yield path


def process_post(path: Path, args: argparse.Namespace) -> str:
    try:
        _, front, rest = read_front_matter(path)
    except ValueError as exc:
        return f"SKIP {path}: {exc}"

    fields = parse_scalar_fields(front)
    image = fields.get("image", "")
    source_image_url = fields.get("source_image_url", "")

    source_url = source_image_url
    source_from_image = False

    if not source_url and image and is_remote(image):
        source_url = image
        source_from_image = True

    if not source_url:
        return f"SKIP {path}: no source_image_url or remote image URL"

    if image and not is_remote(image) and not is_known_placeholder(image) and not args.force:
        return f"SKIP {path}: already using local image {image}"

    output_dir = Path(args.output_dir)
    ext = ".jpg"
    try:
        ext = determine_ext(source_url, None)
        filename = output_name(path, fields, ext)
        local_file = output_dir / filename
        public_path = "/" + local_file.relative_to(Path("static")).as_posix()
    except Exception as exc:
        return f"ERROR {path}: could not determine output path: {exc}"

    if args.dry_run:
        return f"DRY-RUN {path}: would download {source_url} -> {local_file}"

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        data, content_type = download_image(source_url, args.timeout)
        ext = determine_ext(source_url, content_type)
        filename = output_name(path, fields, ext)
        local_file = output_dir / filename
        public_path = "/" + local_file.relative_to(Path("static")).as_posix()

        if local_file.exists() and not args.force:
            # Use the existing file and only update front matter.
            pass
        else:
            local_file.write_bytes(data)

        new_front = front
        if source_from_image and "source_image_url:" not in new_front:
            new_front = set_field(new_front, "source_image_url", source_url, before_key="image")
        new_front = set_field(new_front, "image", public_path)
        if "image_fit:" not in new_front:
            new_front = set_field(new_front, "image_fit", "cover")
        text = "---\n" + new_front.strip() + "\n---" + rest
        path.write_text(text)

        return f"UPDATED {path}: {public_path}"

    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        if args.clear_failed_remote and image and is_remote(image):
            new_front = front
            if source_from_image and "source_image_url:" not in new_front:
                new_front = set_field(new_front, "source_image_url", source_url, before_key="image")
            new_front = remove_field(new_front, "image")
            text = "---\n" + new_front.strip() + "\n---" + rest
            path.write_text(text)
            return f"WARN {path}: download failed ({exc}); removed remote image so placeholder renders"

        return f"ERROR {path}: download failed: {exc}"


def main() -> int:
    args = parse_args()
    results = [process_post(path, args) for path in iter_posts(args)]

    for line in results:
        print(line)

    errors = [line for line in results if line.startswith("ERROR")]
    if errors:
        print("\nSome images could not be downloaded. The CDN URL may have expired.")
        print("Open the original Facebook/Instagram post, save the image manually under static/images/social/,")
        print("then set image: \"/images/social/<filename>\" in that post's front matter.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
