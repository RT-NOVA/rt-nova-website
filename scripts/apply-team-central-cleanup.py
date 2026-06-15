#!/usr/bin/env python3
"""
Apply RT NOVA Team Central cleanup changes.
Run from the repository root:
  python3 scripts/apply-team-central-cleanup.py

This script is intentionally conservative. It updates the teams partial when it
can match known text, and appends CSS overrides for the cleaner Team Central
layout.
"""
from pathlib import Path
import re

root = Path.cwd()
partial = root / "layouts" / "partials" / "page-teams.html"
css = root / "assets" / "css" / "main.css"

if not partial.exists():
    raise SystemExit(f"Missing {partial}")
if not css.exists():
    raise SystemExit(f"Missing {css}")

text = partial.read_text()
orig = text

# 1) Remove the disconnected season helper line if present.
text = text.replace(
    "Rawlings Tigers NOVA seasons run fall through spring. Spring teams are shown first when active.",
    ""
)

# 2) Put the season helper under the selector intro.
text = text.replace(
    "Choose a season to view active and upcoming Rawlings Tigers NOVA teams.",
    "Choose a season to view active and upcoming Rawlings Tigers NOVA teams.<br><span class=\"team-central__season-note\">Rawlings Tigers NOVA seasons run fall through spring.</span>"
)

# 3) Remove common right-side hero art/card blocks if present.
# This catches the generated visual card that only repeats NOVA / Rawlings Tigers.
patterns = [
    r'\n\s*<div class="team-central-hero__visual">.*?</div>\s*',
    r'\n\s*<aside class="team-central-hero__visual">.*?</aside>\s*',
    r'\n\s*<div class="teams-hero__visual">.*?</div>\s*',
    r'\n\s*<aside class="teams-hero__visual">.*?</aside>\s*',
]
for pat in patterns:
    text = re.sub(pat, "\n", text, flags=re.S)

# 4) Replace a large embedded archive details block with a compact archive callout when recognizable.
# If this cannot match, CSS below will still make the archive area less heavy.
archive_match = re.search(r'<details[^>]*class="[^"]*(?:team-central|teams)[^"]*(?:archive|past)[^"]*"[^>]*>.*?</details>', text, flags=re.S|re.I)
if archive_match:
    compact = '''<section class="team-central-archive-callout" aria-labelledby="team-central-archive-title">
  <div>
    <p class="rt-kicker rt-kicker--dark">Past Seasons</p>
    <h2 id="team-central-archive-title">Looking for archived team history?</h2>
    <p>Previous rosters, records, and archived team information can live on a dedicated archive page so Team Central stays focused on current and upcoming teams.</p>
  </div>
  <a class="team-central-archive-callout__link" href="/team-archives/">View Archived Team History →</a>
</section>'''
    text = text[:archive_match.start()] + compact + text[archive_match.end():]

if text != orig:
    partial.with_suffix(partial.suffix + ".bak-teamcentral-cleanup").write_text(orig)
    partial.write_text(text)
    print(f"Updated {partial}")
else:
    print(f"No template text changes made to {partial}; CSS overrides still applied.")

css_block = r'''

/* Team Central cleanup: lighter layout, less nested white boxing */
.team-central__season-note {
  display: block;
  margin-top: 0.45rem;
  color: var(--muted, #6b7280);
  font-size: 0.95rem;
  line-height: 1.5;
}

/* Hide the decorative right-side NOVA wordmark/card in the Team Central hero. */
.team-central-hero__visual,
.teams-hero__visual,
.team-central-hero__card,
.teams-hero__card {
  display: none !important;
}

/* Let the Team Central hero copy use the space naturally after removing the visual card. */
.team-central-hero__inner,
.teams-hero__inner {
  grid-template-columns: minmax(0, 760px) !important;
  justify-content: start;
}

/* Reduce the cards-inside-cards feeling on Spring/Fall team groups. */
.team-central-term,
.teams-term,
.team-season-term,
.team-central__term {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  padding: clamp(1.75rem, 3vw, 2.5rem) 0 !important;
}

.team-central-term + .team-central-term,
.teams-term + .teams-term,
.team-season-term + .team-season-term,
.team-central__term + .team-central__term {
  border-top: 1px solid var(--line, #e5e7eb) !important;
}

/* Team cards still stay card-like, but the outer season groups become lighter. */
.team-card,
.team-central-card,
.teams-card {
  background: #fff;
}

/* Replace heavy archive treatment with a simple callout style. */
.team-central-archive-callout {
  max-width: 1180px;
  margin: clamp(2.5rem, 5vw, 4rem) auto 0;
  padding: clamp(1.4rem, 3vw, 2rem);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  background: #fff;
  border: 1px solid var(--line, #e5e7eb);
  box-shadow: 0 14px 35px rgba(0,0,0,.07);
}

.team-central-archive-callout h2 {
  margin: 0.35rem 0 0.45rem;
}

.team-central-archive-callout p {
  margin: 0;
  color: var(--muted, #6b7280);
  max-width: 720px;
}

.team-central-archive-callout__link {
  flex: 0 0 auto;
  color: var(--brand, #f65f16);
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-decoration: none;
}

@media (max-width: 760px) {
  .team-central-archive-callout {
    align-items: flex-start;
    flex-direction: column;
  }
}
'''

css_text = css.read_text()
marker = "/* Team Central cleanup: lighter layout, less nested white boxing */"
if marker not in css_text:
    css.write_text(css_text.rstrip() + css_block + "\n")
    print(f"Appended cleanup CSS to {css}")
else:
    print("Team Central cleanup CSS already present; skipped append.")
