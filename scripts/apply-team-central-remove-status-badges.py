#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path.cwd()
PARTIAL = ROOT / "layouts" / "partials" / "page-teams.html"
TABLE_PARTIAL = ROOT / "layouts" / "partials" / "team-table-term.html"
CSS = ROOT / "assets" / "css" / "main.css"

STAMP = "teamcentral-remove-status-badges"


def backup(path: Path):
    if path.exists():
        bak = path.with_suffix(path.suffix + f".bak-{STAMP}")
        if not bak.exists():
            bak.write_text(path.read_text())


def remove_status_column_from_team_table(text: str) -> str:
    # Remove table header cells that are exactly/mostly Status.
    text = re.sub(r'(?is)\s*<th[^>]*>\s*Status\s*</th>', '', text)

    # Remove td cells that are status-only and contain one of the status badge classes/words.
    text = re.sub(
        r'(?is)\s*<td[^>]*(?:class="[^"]*(?:status|badge)[^"]*"[^>]*)?>\s*(?:<span[^>]*(?:class="[^"]*(?:status|badge|pill)[^"]*"[^>]*)?>\s*)?(?:active|past|upcoming|coming soon)\s*(?:</span>\s*)?</td>',
        '',
        text,
    )

    # More specific Hugo-template status cell patterns.
    text = re.sub(
        r'(?is)\s*<td[^>]*>\s*<span[^>]*class="[^"]*(?:team-status|team-badge|status-badge|rt-team-status|rt-status|badge|pill)[^"]*"[^>]*>.*?</span>\s*</td>',
        '',
        text,
    )

    # Remove div/mobile status fields if present.
    text = re.sub(
        r'(?is)\s*<div[^>]*class="[^"]*(?:mobile|row|team)[^"]*(?:status)[^"]*"[^>]*>.*?</div>',
        '',
        text,
    )
    return text


def remove_heading_badges(text: str) -> str:
    # Remove visible badges in term headings and season headers. Conservative: only if class name suggests badge/status.
    text = re.sub(
        r'(?is)\s*<span[^>]*class="[^"]*(?:season|term|team|status|badge|pill)[^"]*(?:badge|status|pill)[^"]*"[^>]*>\s*(?:current|upcoming|active|past|coming soon|active teams|past teams|upcoming teams)\s*</span>',
        '',
        text,
    )
    text = re.sub(
        r'(?is)\s*<div[^>]*class="[^"]*(?:season|term|team|status|badge|pill)[^"]*(?:badge|status|pill)[^"]*"[^>]*>\s*(?:current|upcoming|active|past|coming soon|active teams|past teams|upcoming teams)\s*</div>',
        '',
        text,
    )
    return text


def patch_file(path: Path):
    if not path.exists():
        return False
    backup(path)
    text = path.read_text()
    original = text
    text = remove_status_column_from_team_table(text)
    text = remove_heading_badges(text)
    # Remove standalone text phrase if it survived.
    text = re.sub(r'(?is)\s*Spring and fall teams are grouped together under one baseball season\.\s*', '\n', text)
    if text != original:
        path.write_text(text)
    return text != original

changed = []
for p in (PARTIAL, TABLE_PARTIAL):
    if patch_file(p):
        changed.append(str(p))

# Append CSS overrides so any remaining status/badge elements are hidden and the table reflows if template markup survives.
if CSS.exists():
    backup(CSS)
    css_text = CSS.read_text()
    marker = "/* Team Central status-badge cleanup */"
    css_add = r'''

/* Team Central status-badge cleanup */
/* The Current/Upcoming toggle now provides the status context, so hide duplicate badges. */
.rt-team-dashboard .rt-season-status,
.rt-team-dashboard .rt-season-badge,
.rt-team-dashboard .rt-term-status,
.rt-team-dashboard .rt-term-badge,
.rt-team-dashboard .team-status-badge,
.rt-team-dashboard .status-badge,
.rt-team-dashboard .team-badge,
.rt-team-dashboard .team-status,
.team-central-dashboard .rt-season-status,
.team-central-dashboard .rt-season-badge,
.team-central-dashboard .rt-term-status,
.team-central-dashboard .rt-term-badge,
.team-central-dashboard .team-status-badge,
.team-central-dashboard .status-badge,
.team-central-dashboard .team-badge,
.team-central-dashboard .team-status,
.team-central .rt-season-status,
.team-central .rt-season-badge,
.team-central .rt-term-status,
.team-central .rt-term-badge,
.team-central .team-status-badge,
.team-central .status-badge,
.team-central .team-badge,
.team-central .team-status {
  display: none !important;
}

/* Remove the old status column visually if any generated markup remains. */
.rt-team-dashboard table th:first-child:has(+ th),
.rt-team-dashboard table td:first-child:has(+ td),
.team-central-dashboard table th:first-child:has(+ th),
.team-central-dashboard table td:first-child:has(+ td),
.team-central table th:first-child:has(+ th),
.team-central table td:first-child:has(+ td) {
  /* Do not blindly hide the first column unless the template classes above missed it. */
}

/* Cleaner table rhythm after removing status badges. */
.rt-team-dashboard table,
.team-central-dashboard table,
.team-central table {
  border-collapse: separate;
  border-spacing: 0;
}

.rt-team-dashboard tbody tr:nth-child(even),
.team-central-dashboard tbody tr:nth-child(even),
.team-central tbody tr:nth-child(even) {
  background: rgba(248, 250, 252, 0.78);
}

.rt-team-dashboard tbody tr:nth-child(odd),
.team-central-dashboard tbody tr:nth-child(odd),
.team-central tbody tr:nth-child(odd) {
  background: #fff;
}

.rt-team-dashboard tbody tr,
.team-central-dashboard tbody tr,
.team-central tbody tr {
  transition: background-color .18s ease;
}

.rt-team-dashboard tbody tr:hover,
.team-central-dashboard tbody tr:hover,
.team-central tbody tr:hover {
  background: #fff7f1;
}

/* If the table template uses CSS grid columns, collapse from 5 columns to 4. */
.rt-team-table__head,
.rt-team-table__row,
.team-table__head,
.team-table__row,
.team-central-table__head,
.team-central-table__row {
  grid-template-columns: minmax(130px, .8fr) minmax(210px, 1.4fr) minmax(90px, .45fr) minmax(250px, 1.4fr) !important;
}

.rt-team-table__status,
.team-table__status,
.team-central-table__status {
  display: none !important;
}

@media (max-width: 760px) {
  .rt-team-table__head,
  .team-table__head,
  .team-central-table__head {
    display: none !important;
  }

  .rt-team-table__row,
  .team-table__row,
  .team-central-table__row {
    grid-template-columns: 1fr !important;
  }
}
'''
    if marker not in css_text:
        CSS.write_text(css_text + css_add)
        changed.append(str(CSS))

print("Updated Team Central files:")
for item in changed:
    print(f"- {item}")
if not changed:
    print("- No matching files were changed. Check class names in the Teams templates.")
