#!/usr/bin/env python3
from pathlib import Path
import re

root = Path.cwd()
teams = root / "layouts" / "partials" / "page-teams.html"
hero = root / "layouts" / "partials" / "hero.html"
css = root / "assets" / "css" / "main.css"

for p in (teams, css):
    if not p.exists():
        raise SystemExit(f"Missing required file: {p}")

for p in (teams, css):
    bak = p.with_suffix(p.suffix + ".bak-team-card-refresh")
    if not bak.exists():
        bak.write_text(p.read_text())

# Keep this defensive: if the Team Central hero still uses the generic NOVA card, make it optional.
if hero.exists():
    bak = hero.with_suffix(hero.suffix + ".bak-team-card-refresh")
    if not bak.exists():
        bak.write_text(hero.read_text())
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

# Disable the generic right-side hero card for Team Central when the hero partial supports it.
if 'partial "hero.html"' in teams_text and '"show_card" false' not in teams_text:
    def add_show_card_false(match):
        call = match.group(0)
        # Insert before the final closing dict parenthesis.
        return call[:-4] + ' "show_card" false) }}'
    teams_text = re.sub(r'\{\{\s*partial\s+"hero\.html"\s+\(dict.*?\)\s*\}\}', add_show_card_false, teams_text, count=1, flags=re.S)

# Keep the season note in the selector card, not floating above it.
teams_text = teams_text.replace('    <p>{{ $data.season_note }}</p>\n', '')
teams_text = teams_text.replace('    <p>{{ $data.season_note }}</p>\r\n', '')
old_intro = '<p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams.</p>'
new_intro = '<p>Choose a season to view active and upcoming Rawlings Tigers NOVA teams.<span class="rt-season-helper">Rawlings Tigers NOVA seasons run fall through spring.</span></p>'
if old_intro in teams_text and 'rt-season-helper' not in teams_text:
    teams_text = teams_text.replace(old_intro, new_intro)

# Replace the heavy embedded archive cards with a compact archive list when the old archive block is present.
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

css_text = css.read_text()
marker = "/* Team Central social-style card refresh */"
if marker not in css_text:
    css_text = css_text.rstrip() + r'''

/* Team Central social-style card refresh */
.rt-season-helper {
  display: block;
  margin-top: 0.45rem;
  color: var(--rt-muted);
  font-size: 0.95rem;
  line-height: 1.5;
  font-weight: 650;
}

/* Hide the generic right-side NOVA hero card on Team Central only. */
body:has(.rt-team-central) .rt-page-hero__card {
  display: none !important;
}
body:has(.rt-team-central) .rt-page-hero__inner {
  grid-template-columns: minmax(0, 820px) !important;
}

/* Smooth the large Team Central blocks so the page reads less like stacked boxes. */
.rt-team-central .rt-season-selector-card,
.rt-team-central .rt-season-panel__head {
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 18px 42px rgba(6,17,32,.10);
}
.rt-team-central .rt-season-selector-card {
  border-bottom-width: 4px;
}
.rt-team-central .rt-season-panel__head {
  margin-top: clamp(1.15rem, 2.8vw, 2rem);
  margin-bottom: clamp(1.2rem, 2.8vw, 2rem);
}
.rt-team-central .rt-team-term {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  padding: clamp(1.25rem, 3vw, 2.1rem) 0 !important;
}
.rt-team-central .rt-team-term + .rt-team-term {
  border-top: 1px solid var(--rt-line) !important;
}
.rt-team-central .rt-team-term__head {
  padding-bottom: 0.8rem;
  margin-bottom: 1rem;
}
.rt-team-central .rt-card-grid {
  gap: clamp(0.95rem, 2vw, 1.35rem);
}

/* Team cards: closer to Social Hub cards, but still clearly team/profile cards. */
.rt-team-central .rt-team-card,
.rt-team-card--central,
.rt-team-card--archive {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0;
  padding: 0 !important;
  overflow: hidden;
  border: 1px solid rgba(6,17,32,.09) !important;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 18px 38px rgba(6,17,32,.09);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.rt-team-central .rt-team-card:hover,
.rt-team-card--central:hover {
  transform: translateY(-2px);
  border-color: rgba(246,95,22,.24) !important;
  box-shadow: 0 22px 46px rgba(6,17,32,.13);
}
.rt-team-central .rt-team-card__top {
  min-height: 44px;
  padding: 1rem 1rem .35rem;
  align-items: flex-start;
}
.rt-team-central .rt-team-card h3 {
  margin: 0;
  padding: 0 1rem .75rem;
  font-size: clamp(1.45rem, 2.2vw, 1.75rem);
  line-height: 1;
}
.rt-team-central .rt-team-record {
  color: var(--rt-muted);
  font-size: .9rem;
  line-height: 1;
}
.rt-team-central .rt-person-inline {
  margin: 0 1rem 1rem;
  padding: .85rem;
  border: 1px solid var(--rt-line);
  border-radius: 14px;
  background: linear-gradient(180deg,#fff,#fafafa);
}
.rt-team-central .rt-person-inline img {
  width: 54px;
  height: 64px;
  border-radius: 10px;
  box-shadow: 0 0 0 1px var(--rt-line);
}
.rt-team-central .rt-person-inline small {
  font-size: .66rem;
  letter-spacing: .08em;
}
.rt-team-central .rt-person-inline strong {
  font-size: .92rem;
  line-height: 1.15;
}
.rt-team-central .rt-link-row {
  margin-top: auto;
  padding: .9rem 1rem 1rem;
  border-top: 1px solid var(--rt-line);
  background: #fff;
  gap: .45rem;
}
.rt-team-central .rt-link-row a {
  min-height: 32px;
  border-radius: 999px;
  padding: .45rem .75rem;
  font-size: .68rem;
  line-height: 1;
}
.rt-team-central .rt-link-row .rt-muted,
.rt-team-central .rt-muted {
  color: var(--rt-muted);
  font-size: .95rem;
  font-weight: 650;
}
.rt-team-central .rt-empty-team-note {
  border: 1px solid rgba(6,17,32,.08);
  border-radius: 16px;
  background: rgba(255,255,255,.68) !important;
  box-shadow: 0 14px 30px rgba(6,17,32,.06);
}

/* Compact archive treatment: keep history available without making /teams/ feel like an archive page. */
.rt-team-archive--compact {
  padding-top: 0 !important;
}
.rt-archive-compact {
  background: #fff;
  border: 1px solid var(--rt-line);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 18px 42px rgba(6,17,32,.08);
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
  .rt-team-central .rt-season-selector-card,
  .rt-team-central .rt-season-panel__head {
    border-radius: 14px;
  }
  .rt-team-central .rt-team-card,
  .rt-team-card--central,
  .rt-team-card--archive {
    border-radius: 16px;
  }
  .rt-team-central .rt-link-row a {
    flex: 1 1 auto;
    justify-content: center;
  }
  .rt-archive-compact summary span,
  .rt-archive-compact__item {
    align-items: flex-start;
    flex-direction: column;
  }
}
'''
    css.write_text(css_text + "\n")

print("Team Central social-style cards applied.")
print("Backups created with .bak-team-card-refresh suffix if they did not already exist.")
