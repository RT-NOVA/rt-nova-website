#!/usr/bin/env python3
from pathlib import Path
import re

layout_path = Path("layouts/partials/page-tryouts.html")
css_path = Path("assets/css/tryouts.css")

if not layout_path.exists():
    raise SystemExit(f"Missing {layout_path}")

text = layout_path.read_text()

# 1) Replace the badge-style Session cell with a cleaner text + dot treatment.
badge_block = re.compile(
    r'(?P<indent>\s*)\{\{ \$sessionType := \.type \| default "Evaluation" \}\}\s*\n'
    r'\s*\{\{ \$sessionTypeLower := lower \$sessionType \}\}\s*\n'
    r'\s*\{\{ \$sessionClass := "rt-tryout-session-badge" \}\}\s*\n'
    r'\s*\{\{ if in \$sessionTypeLower "formal" \}\}\{\{ \$sessionClass = printf "%s rt-tryout-session-badge--formal" \$sessionClass \}\}\{\{ else if in \$sessionTypeLower "open" \}\}\{\{ \$sessionClass = printf "%s rt-tryout-session-badge--open" \$sessionClass \}\}\{\{ end \}\}\s*\n'
    r'\s*<div role="cell" data-label="Session">\s*\n'
    r'\s*<span class="\{\{ \$sessionClass \}\}">\{\{ \$sessionType \}\}</span>\s*\n'
    r'\s*</div>',
    re.MULTILINE,
)

clean_session = '''\\g<indent>{{ $sessionType := .type | default "Evaluation" }}
\\g<indent>{{ $sessionTypeLower := lower $sessionType }}
\\g<indent>{{ $sessionClass := "rt-tryout-session-type" }}
\\g<indent>{{ if in $sessionTypeLower "formal" }}{{ $sessionClass = printf "%s rt-tryout-session-type--formal" $sessionClass }}{{ else if in $sessionTypeLower "open" }}{{ $sessionClass = printf "%s rt-tryout-session-type--open" $sessionClass }}{{ end }}
\\g<indent><div role="cell" data-label="Session">
\\g<indent>  <span class="{{ $sessionClass }}">{{ $sessionType }}</span>
\\g<indent></div>'''

text, badge_count = badge_block.subn(clean_session, text)

# Fallback if the badge script was not applied or the current template still has plain {{ .type }}.
if badge_count == 0 and "rt-tryout-session-type" not in text:
    plain_session = re.compile(
        r'(?P<indent>\s*)<div role="cell" data-label="Session">\s*\n'
        r'\s*<span>\{\{ \.type \}\}</span>\s*\n'
        r'\s*</div>',
        re.MULTILINE,
    )
    text, plain_count = plain_session.subn(clean_session, text)
else:
    plain_count = 0

# 2) Add a Directions column header if it does not exist.
if 'data-label="Directions"' not in text and '>Directions<' not in text:
    text, header_count = re.subn(
        r'(?P<indent>\s*)<div role="columnheader">Location</div>',
        r'\g<indent><div role="columnheader">Location</div>\n\g<indent><div role="columnheader" class="rt-tryout-directions-head">Directions</div>',
        text,
        count=1,
    )
else:
    header_count = 0

# 3) Add clickable directions icon after the Location cell if it does not exist.
if 'data-label="Directions"' not in text:
    location_cell = re.compile(
        r'(?P<block>(?P<indent>\s*)<div role="cell" data-label="Location">\s*\n'
        r'\s*<span>\{\{ \.location \}\}</span>\s*\n'
        r'\s*</div>)',
        re.MULTILINE,
    )

    directions_cell = r'''\g<block>
\g<indent>{{ $directionsUrl := .directions_url | default (printf "https://www.google.com/maps/search/?api=1&query=%s" (.location | urlquery)) }}
\g<indent><div role="cell" data-label="Directions" class="rt-tryout-directions-cell">
\g<indent>  <a class="rt-tryout-directions-link" href="{{ $directionsUrl }}" target="_blank" rel="noopener" aria-label="Get directions to {{ .location }}">
\g<indent>    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
\g<indent>      <path d="M9 18l-6 3V6l6-3 6 3 6-3v15l-6 3-6-3z"></path>
\g<indent>      <path d="M9 3v15"></path>
\g<indent>      <path d="M15 6v15"></path>
\g<indent>    </svg>
\g<indent>    <span class="rt-sr-only">Directions</span>
\g<indent>  </a>
\g<indent></div>'''

    text, directions_count = location_cell.subn(directions_cell, text)
else:
    directions_count = 0

layout_path.write_text(text)
print(f"Updated {layout_path}")
print(f"- Converted badge session markup: {badge_count}")
print(f"- Converted plain session markup: {plain_count}")
print(f"- Added Directions header: {header_count}")
print(f"- Added Directions cells: {directions_count}")

# 4) CSS cleanup and new styling.
css_path.parent.mkdir(parents=True, exist_ok=True)
css = css_path.read_text() if css_path.exists() else ""

# Remove old badge styles if they exist.
css = re.sub(r'\n/\* Tryout session type badges \*/[\s\S]*?(?=\n/\*|\Z)', '\n', css)
css = re.sub(r'\n\.rt-tryout-session-badge(?:--open|--formal)? \{[\s\S]*?\}\n', '\n', css)

# Remove older clean/directions patch if rerun.
css = re.sub(r'\n/\* Clean tryout session type \+ directions \*/[\s\S]*?(?=\n/\*|\Z)', '\n', css)

css = css.rstrip() + r'''

/* Clean tryout session type + directions */
.rt-tryout-session-type {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  color: var(--rt-navy);
  font-weight: 900;
  letter-spacing: .01em;
  white-space: nowrap;
}

.rt-tryout-session-type::before {
  content: "";
  width: .45rem;
  height: .45rem;
  border-radius: 999px;
  background: currentColor;
  flex: 0 0 auto;
}

.rt-tryout-session-type--open {
  color: var(--rt-orange);
}

.rt-tryout-session-type--formal {
  color: var(--rt-navy);
}

.rt-tryout-directions-head,
.rt-tryout-directions-cell {
  text-align: right;
  justify-content: flex-end;
}

.rt-tryout-directions-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.15rem;
  height: 2.15rem;
  border: 1px solid rgba(7, 16, 31, .16);
  background: #fff;
  color: var(--rt-navy);
  text-decoration: none;
  transition: border-color .18s ease, color .18s ease, transform .18s ease, box-shadow .18s ease;
}

.rt-tryout-directions-link:hover,
.rt-tryout-directions-link:focus-visible {
  border-color: var(--rt-orange);
  color: var(--rt-orange);
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(7, 16, 31, .12);
}

.rt-tryout-directions-link svg {
  width: 1.05rem;
  height: 1.05rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.rt-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  white-space: nowrap;
  border: 0;
  clip: rect(0, 0, 0, 0);
}

/* Add a compact Directions column to the tryout schedule table. */
.rt-tryout-schedule-table [role="row"],
.rt-tryout-schedule-grid [role="row"],
.rt-tryout-schedule-header,
.rt-tryout-schedule-row {
  grid-template-columns: minmax(150px, .9fr) minmax(230px, 1.45fr) minmax(135px, .75fr) minmax(280px, 1.65fr) 72px;
}

@media (max-width: 980px) {
  .rt-tryout-directions-head {
    display: none;
  }

  .rt-tryout-directions-cell {
    text-align: left;
    justify-content: flex-start;
  }

  .rt-tryout-directions-cell::before {
    content: attr(data-label);
  }
}
'''

css_path.write_text(css)
print(f"Updated {css_path}")
print("Done. Run: hugo server -D --disableFastRender")
