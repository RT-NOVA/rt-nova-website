#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-team-table-compact")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central compact table tuning */"
append = r'''

/* Team Central compact table tuning */
body:has(.rt-team-central--table) .rt-team-central--table {
  padding-top: clamp(2rem, 4vw, 3.25rem);
  padding-bottom: clamp(2rem, 4vw, 3rem);
}

body:has(.rt-team-central--table) .rt-team-central__intro {
  margin-bottom: clamp(1rem, 2vw, 1.35rem);
}

body:has(.rt-team-central--table) .rt-team-central__intro h2 {
  font-size: clamp(2.65rem, 5.2vw, 4.35rem);
  letter-spacing: .075em;
}

body:has(.rt-team-central--table) .rt-team-central__intro p {
  margin-block: .25rem;
}

body:has(.rt-team-central--table) .rt-season-selector-card--compact {
  padding: clamp(1rem, 2vw, 1.35rem);
  border-radius: 16px;
  box-shadow: 0 12px 28px rgba(6,17,32,.07);
}

body:has(.rt-team-central--table) .rt-season-selector-card--compact h3 {
  font-size: clamp(1.75rem, 3.4vw, 2.65rem);
  letter-spacing: .06em;
}

body:has(.rt-team-central--table) .rt-season-panels {
  margin-top: clamp(1rem, 2.2vw, 1.4rem);
}

body:has(.rt-team-central--table) .rt-season-panel__head--table {
  margin: 0 0 clamp(1.1rem, 2.5vw, 1.55rem);
  padding: clamp(1.1rem, 2.5vw, 1.55rem);
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(6,17,32,.12);
}

body:has(.rt-team-central--table) .rt-season-panel__head--table h2 {
  margin-top: .42rem;
  font-size: clamp(2.35rem, 5.4vw, 4rem);
  letter-spacing: .085em;
}

body:has(.rt-team-central--table) .rt-season-panel__head--table p {
  line-height: 1.35;
}

body:has(.rt-team-central--table) .rt-team-term--table {
  margin: clamp(1.15rem, 2.2vw, 1.6rem) 0 clamp(1.35rem, 2.8vw, 2rem);
}

body:has(.rt-team-central--table) .rt-team-term__head--table {
  padding-bottom: .55rem;
}

body:has(.rt-team-central--table) .rt-team-term__head--table h3 {
  font-size: clamp(1.85rem, 3.8vw, 2.85rem);
  letter-spacing: .07em;
}

body:has(.rt-team-central--table) .rt-team-table {
  margin-top: .7rem;
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(6,17,32,.065);
}

body:has(.rt-team-central--table) .rt-team-table__head,
body:has(.rt-team-central--table) .rt-team-row {
  grid-template-columns: 110px minmax(110px,.7fr) minmax(220px,1.05fr) 90px minmax(250px,1.2fr);
  gap: .85rem;
}

body:has(.rt-team-central--table) .rt-team-table__head {
  min-height: 42px;
  padding-inline: .95rem;
}

body:has(.rt-team-central--table) .rt-team-row {
  min-height: 72px;
  padding: .55rem .95rem;
}

body:has(.rt-team-central--table) .rt-team-row__coach {
  gap: .7rem;
}

body:has(.rt-team-central--table) .rt-team-row__coach img {
  width: 44px;
  height: 44px;
  border-radius: 10px;
}

body:has(.rt-team-central--table) .rt-team-row__team strong {
  font-size: 1.02rem;
}

body:has(.rt-team-central--table) .rt-team-row__coach strong {
  font-size: .88rem;
}

body:has(.rt-team-central--table) .rt-team-row__coach small {
  margin-bottom: .08rem;
  font-size: .62rem;
}

body:has(.rt-team-central--table) .rt-team-row__links {
  gap: .32rem;
}

body:has(.rt-team-central--table) .rt-team-row__links a {
  min-height: 28px;
  padding: .38rem .62rem;
  font-size: .62rem;
}

body:has(.rt-team-central--table) .rt-badge {
  padding: .32rem .62rem;
  font-size: .62rem;
}

body:has(.rt-team-central--table) .rt-empty-team-note--table {
  margin-top: .7rem;
  padding: .85rem 1rem;
  border-radius: 14px;
  box-shadow: none;
}

body:has(.rt-team-central--table) .rt-team-join-band {
  padding-top: clamp(2.2rem, 4vw, 3.25rem);
  padding-bottom: clamp(2.2rem, 4vw, 3.25rem);
}

body:has(.rt-team-central--table) .rt-team-join-band h2 {
  font-size: clamp(2rem, 4.6vw, 3.25rem);
}

@media (max-width: 1080px) {
  body:has(.rt-team-central--table) .rt-team-table__head,
  body:has(.rt-team-central--table) .rt-team-row {
    grid-template-columns: 95px minmax(90px,.6fr) minmax(190px,1fr) 80px minmax(190px,1fr);
    gap: .7rem;
  }
}

@media (max-width: 820px) {
  body:has(.rt-team-central--table) .rt-team-central__intro {
    text-align: left;
  }
  body:has(.rt-team-central--table) .rt-season-panel__head--table,
  body:has(.rt-team-central--table) .rt-season-selector-card--compact {
    gap: .85rem;
  }
  body:has(.rt-team-central--table) .rt-team-row {
    padding: .9rem;
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
    print("Appended Team Central compact table tuning to assets/css/main.css")
else:
    print("Team Central compact table tuning already present; no changes made.")
