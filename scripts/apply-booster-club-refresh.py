#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path.cwd()
SCRIPT_DIR = Path(__file__).resolve().parent
PATCH_ROOT = SCRIPT_DIR.parent

files_to_copy = [
    (PATCH_ROOT / "content" / "booster-club.md", ROOT / "content" / "booster-club.md"),
    (PATCH_ROOT / "layouts" / "partials" / "page-booster-club.html", ROOT / "layouts" / "partials" / "page-booster-club.html"),
    (PATCH_ROOT / "docs" / "BOOSTER_CLUB_README.md", ROOT / "docs" / "BOOSTER_CLUB_README.md"),
]

for src, dst in files_to_copy:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Updated {dst.relative_to(ROOT)}")

single = ROOT / "layouts" / "_default" / "single.html"
if single.exists():
    text = single.read_text()
    branch = '  {{ else if eq $template "booster-club" }}{{ partial "page-booster-club.html" . }}\n'
    if 'eq $template "booster-club"' not in text:
        anchors = [
            '  {{ else if eq $template "family-hub" }}{{ partial "page-family-hub.html" . }}\n',
            '  {{ else if eq $template "about" }}{{ partial "page-about.html" . }}\n',
            '  {{ else if eq $template "accolades" }}{{ partial "page-accolades.html" . }}\n',
        ]
        inserted = False
        for anchor in anchors:
            if anchor in text:
                text = text.replace(anchor, anchor + branch, 1)
                inserted = True
                break
        if not inserted:
            fallback = '  {{ else }}\n'
            if fallback in text:
                text = text.replace(fallback, branch + fallback, 1)
                inserted = True
        if not inserted:
            raise SystemExit("Could not find a safe insertion point in layouts/_default/single.html")
        single.write_text(text)
        print("Updated layouts/_default/single.html with booster-club template branch")
    else:
        print("layouts/_default/single.html already has booster-club template branch")
else:
    raise SystemExit("Missing layouts/_default/single.html")

print("Booster Club refresh applied.")
