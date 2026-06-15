#!/usr/bin/env python3
from pathlib import Path
import re

root = Path.cwd()
hero = root / "layouts" / "partials" / "hero.html"
teams = root / "layouts" / "partials" / "page-teams.html"
css = root / "assets" / "css" / "main.css"

for p in (hero, teams, css):
    if not p.exists():
        raise SystemExit(f"Missing required file: {p}")

# Backup once
for p in (hero, teams, css):
    bak = p.with_suffix(p.suffix + ".bak-teamcentral-corrections")
    if not bak.exists():
        bak.write_text(p.read_text())

# 1) Make generic hero card optional, then disable it for Team Central.
hero_text = hero.read_text()
if "show_card" not in hero_text:
    hero_text = hero_text.replace(
        '    <div class="rt-page-hero__card" aria-hidden="true">\n'
        '      <span>NOVA</span>\n'
        '      <strong>Rawlings Tigers</strong>\n'
        '      <em>Develop • Compete • Represent</em>\n'
        '    </div>',
        '    {{ if ne .show_card false }}\n'
        '    <div class="rt-page-hero__card" aria-hidden="true">\n'
        '      <span>NOVA</span>\n'
        '      <strong>Rawlings Tigers</strong>\n'
        '      <em>Develop • Compete • Represent</em>\n'
        '    </div>\n'
        '    {{ end }}'
    )
hero.write_text(hero_text)

teams_text = teams.read_text()

# Add show_card false to the Team Central hero partial call.
if 'partial "hero.html"' in teams_text and '"show_card" false' not in teams_text:
    def add_show_card_false(match):
        call = match.group(0)
        return call[:-4] + ' "show_card" false) }}'
    teams_text = re.sub(r'\{\{\s*partial\s+"hero\.html"\s+\(dict.*?\)\s*\}\}', add_show_card_false, teams_text, count=1)

# Remove the duplicate/disconnected season helper from the centered intro.
teams_text = teams_text.replace('    <p>{{ $data.season_note }}</p>\n', '')
teams_text = teams_text.replace('    <p>{{ $data.season_note }}</p>\r\n', '')

# Add the season helper directly under the selector intro.
old_intro = '<p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams.</p>'
new_intro = '<p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams.<span class="rt-season-helper">Rawlings Tigers NOVA seasons run fall through spring.</span></p>'
if old_intro in teams_text and 'rt-season-helper' not in teams_text:
    teams_text = teams_text.replace(old_intro, new_intro)

# Replace the heavy archive section with a compact archive callout/list.
archive_start = teams_text.find('{{ with $data.past_seasons }}')
script_start = teams_text.find('<script>', archive_start if archive_start != -1 else 0)
if archive_start != -1 and script_start != -1 and 'rt-team-archive--compact' not in teams_text:
    compact_archive = '''{{ with $data.past_seasons }}
<section class="rt-section rt-team-archive rt-team-archive--compact">
  <div class="rt-container">
    <details class="rt-archive-compact">
      <summary>
        <span>
          <small>Past Seasons</small>
          <strong>View archived team history</strong>
        </span>
      </summary>
      <div class="rt-archive-compact__list">
        {{ range . }}
          <div class="rt-archive-compact__item">
            <strong>{{ .label }}</strong>
            <span>{{ .cycle }}</span>
          </div>
        {{ end }}
      </div>
    </details>
  </div>
</section>
{{ end }}

'''
    teams_text = teams_text[:archive_start] + compact_archive + teams_text[script_start:]

teams.write_text(teams_text)

# 2) Append exact CSS corrections for the current rt-* Team Central classes.
css_text = css.read_text()
marker = "/* Team Central corrections v2 */"
if marker not in css_text:
    css_text = css_text.rstrip() + r'''

/* Team Central corrections v2 */
.rt-season-helper {
  display: block;
  margin-top: 0.45rem;
  color: var(--rt-muted);
  font-size: 0.95rem;
  line-height: 1.5;
  font-weight: 650;
}

/* Team Central should not show the generic right-side NOVA hero card. */
body:has(.rt-team-central) .rt-page-hero__card {
  display: none !important;
}
body:has(.rt-team-central) .rt-page-hero__inner {
  grid-template-columns: minmax(0, 820px) !important;
}

/* Lighten Spring/Fall group wrappers so the page feels less blocky. */
.rt-team-central .rt-team-term {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  padding: clamp(1.5rem, 3vw, 2.25rem) 0 !important;
}
.rt-team-central .rt-team-term + .rt-team-term {
  border-top: 1px solid var(--rt-line) !important;
}
.rt-team-central .rt-team-term__head {
  padding-bottom: 0.85rem;
  margin-bottom: 1rem;
}
.rt-team-central .rt-empty-team-note {
  background: rgba(255,255,255,.58) !important;
}

/* Compact archive treatment: keep past seasons available, but do not embed a full archive page. */
.rt-team-archive--compact {
  padding-top: 0 !important;
}
.rt-archive-compact {
  background: #fff;
  border: 1px solid var(--rt-line);
  box-shadow: var(--rt-shadow-soft);
}
.rt-archive-compact summary {
  cursor: pointer;
  list-style: none;
  padding: clamp(1rem, 2.5vw, 1.35rem);
}
.rt-archive-compact summary::-webkit-details-marker {
  display: none;
}
.rt-archive-compact summary span {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.rt-archive-compact summary small {
  color: var(--rt-orange-dark);
  font-size: .72rem;
  font-weight: 950;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.rt-archive-compact summary strong {
  color: var(--rt-navy);
  font-family: var(--rt-display);
  font-size: clamp(1.2rem, 2.4vw, 1.65rem);
  line-height: 1;
  text-transform: uppercase;
}
.rt-archive-compact__list {
  display: grid;
  gap: .75rem;
  border-top: 1px solid var(--rt-line);
  padding: clamp(1rem, 2.5vw, 1.35rem);
}
.rt-archive-compact__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .85rem 0;
  border-bottom: 1px solid var(--rt-line);
}
.rt-archive-compact__item:last-child {
  border-bottom: 0;
}
.rt-archive-compact__item strong {
  color: var(--rt-navy);
  font-weight: 950;
}
.rt-archive-compact__item span {
  color: var(--rt-muted);
  font-weight: 700;
}

@media (max-width: 760px) {
  body:has(.rt-team-central) .rt-page-hero__inner {
    grid-template-columns: 1fr !important;
  }
  .rt-archive-compact summary span,
  .rt-archive-compact__item {
    align-items: flex-start;
    flex-direction: column;
  }
}
'''
    css.write_text(css_text + "\n")

print("Team Central corrections applied.")
print("Backups created with .bak-teamcentral-corrections suffix if they did not already exist.")
