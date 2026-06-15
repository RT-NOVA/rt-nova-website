#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path.cwd()


def backup(path: Path):
    if path.exists():
        bak = path.with_suffix(path.suffix + '.bak-teamcentral-selector-cleanup')
        if not bak.exists():
            bak.write_text(path.read_text())

# 1) Clean the teams data intro and force current season as the default.
teams_path = ROOT / 'data' / 'teams.yaml'
if teams_path.exists():
    backup(teams_path)
    text = teams_path.read_text()
    text = re.sub(
        r'^intro:\s*"[^"]*"',
        'intro: "Explore Rawlings Tigers NOVA teams by baseball season."',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(r'^default_season:\s*"[^"]*"', 'default_season: "2026"', text, count=1, flags=re.M)
    teams_path.write_text(text)
else:
    raise SystemExit('Missing data/teams.yaml')

# 2) Remove the duplicate Team Central intro block and move the helper text into the Select Season card.
page_path = ROOT / 'layouts' / 'partials' / 'page-teams.html'
if page_path.exists():
    backup(page_path)
    text = page_path.read_text()

    # Remove duplicate centered Team Central intro section below the hero.
    text = re.sub(
        r'\n\s*<div class="rt-container rt-team-central__intro[^>]*>\s*\n\s*<h2>Team Central</h2>\s*\n\s*<p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams\.</p>\s*\n\s*<p class="rt-season-helper">Rawlings Tigers NOVA seasons run fall through spring\.</p>\s*\n\s*</div>\s*\n',
        '\n',
        text,
        count=1,
        flags=re.S,
    )

    # Add the helper copy inside the Select Season heading area if it is not already there.
    if 'rt-season-dashboard__selector-copy' not in text:
        text = text.replace(
            '        <div>\n          <h3>Select Season</h3>\n        </div>',
            '        <div class="rt-season-dashboard__selector-copy">\n          <h3>Select Season</h3>\n          <p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams.</p>\n          <p>Rawlings Tigers NOVA seasons run fall through spring.</p>\n        </div>',
            1,
        )

    page_path.write_text(text)
else:
    raise SystemExit('Missing layouts/partials/page-teams.html')

# 3) Add CSS polish for the selector copy inside the white card.
css_path = ROOT / 'assets' / 'css' / 'main.css'
if css_path.exists():
    backup(css_path)
    css = css_path.read_text()
    marker = '/* Team Central selector/hero cleanup */'
    if marker not in css:
        css += '''\n\n/* Team Central selector/hero cleanup */\n.rt-team-central--dashboard .rt-season-dashboard__selector-copy {\n  max-width: 620px;\n}\n\n.rt-team-central--dashboard .rt-season-dashboard__selector-copy h3 {\n  margin-bottom: .55rem;\n}\n\n.rt-team-central--dashboard .rt-season-dashboard__selector-copy p {\n  margin: .15rem 0 0;\n  color: var(--muted, #6b7280);\n  font-weight: 700;\n  letter-spacing: .01em;\n  line-height: 1.45;\n  text-transform: none;\n}\n\n@media (max-width: 900px) {\n  .rt-team-central--dashboard .rt-season-dashboard__top--toggle {\n    gap: 1rem;\n  }\n\n  .rt-team-central--dashboard .rt-season-dashboard__selector-copy {\n    max-width: none;\n  }\n}\n'''
        css_path.write_text(css)
else:
    raise SystemExit('Missing assets/css/main.css')

print('Team Central selector/hero cleanup applied.')
print('Updated:')
print('  data/teams.yaml')
print('  layouts/partials/page-teams.html')
print('  assets/css/main.css')
