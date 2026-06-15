#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-team-season-dashboard")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central unified season dashboard */"
append = r'''

/* Team Central unified season dashboard */
body:has(.rt-team-central--dashboard) .rt-team-central--dashboard {
  padding-top: clamp(2.4rem, 4vw, 4rem);
  padding-bottom: clamp(2.5rem, 5vw, 4.5rem);
}

body:has(.rt-team-central--dashboard) .rt-team-central__intro--compact {
  max-width: 860px;
  margin: 0 auto clamp(1.35rem, 2.8vw, 2rem);
  text-align: center;
}

body:has(.rt-team-central--dashboard) .rt-team-central__intro--compact h2 {
  margin: .25rem 0 .55rem;
  font-size: clamp(2.8rem, 5.4vw, 4.8rem);
  line-height: .95;
  letter-spacing: .075em;
}

body:has(.rt-team-central--dashboard) .rt-team-central__intro--compact p {
  margin: .25rem 0;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard {
  overflow: hidden;
  border: 1px solid rgba(6,17,32,.12);
  border-radius: 22px;
  background: #fff;
  box-shadow: 0 24px 56px rgba(6,17,32,.10);
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__top {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(280px, 420px);
  align-items: end;
  gap: clamp(1rem, 3vw, 2rem);
  padding: clamp(1.1rem, 2.5vw, 1.75rem) clamp(1.1rem, 3vw, 2rem);
  border-bottom: 4px solid var(--rt-orange, #f15a24);
  background: #fff;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__top h3 {
  margin: .25rem 0 .3rem;
  color: var(--rt-navy, #07111f);
  font-size: clamp(2rem, 4vw, 3.2rem);
  line-height: .95;
  letter-spacing: .08em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__top p {
  max-width: 620px;
  margin: 0;
  color: var(--rt-muted, #5d6675);
  font-weight: 700;
}

body:has(.rt-team-central--dashboard) .rt-season-select-label {
  display: grid;
  gap: .35rem;
}

body:has(.rt-team-central--dashboard) .rt-season-select-label span {
  color: var(--rt-orange-dark, #a94724);
  font-size: .68rem;
  font-weight: 900;
  letter-spacing: .22em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-season-select {
  width: 100%;
  min-height: 42px;
  border: 1px solid rgba(6,17,32,.18);
  border-radius: 10px;
  background: #fff;
  color: var(--rt-navy, #07111f);
  font-weight: 900;
  letter-spacing: .02em;
}

body:has(.rt-team-central--dashboard) .rt-season-panels {
  margin: 0;
}

body:has(.rt-team-central--dashboard) .rt-season-panel--dashboard {
  padding: 0;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary {
  display: grid;
  grid-template-columns: minmax(260px,.75fr) minmax(0,1fr);
  align-items: center;
  gap: clamp(1rem, 3vw, 2rem);
  padding: clamp(1.15rem, 2.8vw, 2rem);
  background: #07111f;
  color: #fff;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary h2 {
  margin: .5rem 0 .25rem;
  color: #fff;
  font-size: clamp(2.5rem, 5vw, 4.4rem);
  line-height: .9;
  letter-spacing: .1em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary p {
  margin: 0;
  color: rgba(255,255,255,.78);
  font-weight: 800;
  line-height: 1.45;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary > p {
  max-width: 620px;
  font-size: clamp(.98rem, 1.4vw, 1.1rem);
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__terms {
  padding: clamp(1rem, 2.4vw, 1.7rem);
  background: linear-gradient(180deg, rgba(247,248,250,.92), rgba(255,255,255,1));
}

body:has(.rt-team-central--dashboard) .rt-team-term--dashboard {
  margin: 0;
}

body:has(.rt-team-central--dashboard) .rt-team-term--dashboard + .rt-team-term--dashboard {
  margin-top: clamp(1rem, 2.4vw, 1.75rem);
  padding-top: clamp(1rem, 2.4vw, 1.75rem);
  border-top: 1px solid rgba(6,17,32,.10);
}

body:has(.rt-team-central--dashboard) .rt-team-term__head--dashboard {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: .75rem;
}

body:has(.rt-team-central--dashboard) .rt-team-term__head--dashboard h3 {
  margin: .2rem 0 0;
  color: var(--rt-navy, #07111f);
  font-size: clamp(1.8rem, 3.6vw, 2.95rem);
  line-height: .95;
  letter-spacing: .075em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-team-table--dashboard {
  overflow: hidden;
  border: 1px solid rgba(6,17,32,.10);
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 10px 28px rgba(6,17,32,.055);
}

body:has(.rt-team-central--dashboard) .rt-team-table__head,
body:has(.rt-team-central--dashboard) .rt-team-row {
  display: grid;
  grid-template-columns: 110px minmax(120px,.55fr) minmax(250px,1fr) 90px minmax(280px,1.25fr);
  align-items: center;
  gap: .9rem;
}

body:has(.rt-team-central--dashboard) .rt-team-table__head {
  min-height: 42px;
  padding: .72rem 1rem;
  background: #f2f4f7;
  color: #454d5c;
  font-size: .68rem;
  font-weight: 900;
  letter-spacing: .16em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-team-row {
  min-height: 70px;
  padding: .62rem 1rem;
  border-top: 1px solid rgba(6,17,32,.075);
}

body:has(.rt-team-central--dashboard) .rt-team-row:first-child {
  border-top: 0;
}

body:has(.rt-team-central--dashboard) .rt-team-row__team strong,
body:has(.rt-team-central--dashboard) .rt-team-row__record strong,
body:has(.rt-team-central--dashboard) .rt-team-row__coach strong {
  color: var(--rt-navy, #07111f);
  font-weight: 900;
}

body:has(.rt-team-central--dashboard) .rt-team-row__coach {
  display: flex;
  align-items: center;
  gap: .7rem;
}

body:has(.rt-team-central--dashboard) .rt-team-row__coach img {
  width: 44px;
  height: 44px;
  flex: 0 0 44px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 7px 16px rgba(6,17,32,.16);
}

body:has(.rt-team-central--dashboard) .rt-team-row__coach span {
  display: grid;
  gap: .06rem;
}

body:has(.rt-team-central--dashboard) .rt-team-row__coach small {
  color: var(--rt-orange-dark, #a94724);
  font-size: .62rem;
  font-weight: 900;
  letter-spacing: .08em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-team-row__links {
  display: flex;
  flex-wrap: wrap;
  gap: .38rem;
}

body:has(.rt-team-central--dashboard) .rt-team-row__links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 28px;
  padding: .34rem .65rem;
  border: 1px solid rgba(6,17,32,.13);
  border-radius: 999px;
  background: #fff;
  color: var(--rt-navy, #07111f);
  font-size: .62rem;
  font-weight: 900;
  letter-spacing: .08em;
  text-decoration: none;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-team-row__links a:hover {
  border-color: var(--rt-orange, #f15a24);
  color: var(--rt-orange-dark, #a94724);
}

body:has(.rt-team-central--dashboard) .rt-empty-team-note--dashboard {
  display: grid;
  gap: .18rem;
  margin-top: .7rem;
  padding: .9rem 1rem;
  border: 1px solid rgba(6,17,32,.07);
  border-radius: 14px;
  background: rgba(255,255,255,.72);
  color: var(--rt-muted, #5d6675);
}

body:has(.rt-team-central--dashboard) .rt-empty-team-note--dashboard strong {
  color: var(--rt-navy, #07111f);
}

body:has(.rt-team-central--dashboard) .rt-team-join-band--compact {
  padding-top: clamp(2.2rem, 4vw, 3.5rem);
  padding-bottom: clamp(2.2rem, 4vw, 3.5rem);
}

@media (max-width: 1080px) {
  body:has(.rt-team-central--dashboard) .rt-team-table__head,
  body:has(.rt-team-central--dashboard) .rt-team-row {
    grid-template-columns: 92px minmax(92px,.6fr) minmax(210px,1fr) 74px minmax(210px,1fr);
    gap: .65rem;
  }
}

@media (max-width: 860px) {
  body:has(.rt-team-central--dashboard) .rt-team-central__intro--compact {
    text-align: left;
  }

  body:has(.rt-team-central--dashboard) .rt-season-dashboard__top,
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary {
    grid-template-columns: 1fr;
    align-items: start;
  }

  body:has(.rt-team-central--dashboard) .rt-team-table__head {
    display: none;
  }

  body:has(.rt-team-central--dashboard) .rt-team-table--dashboard {
    display: grid;
    gap: .75rem;
    border: 0;
    background: transparent;
    box-shadow: none;
  }

  body:has(.rt-team-central--dashboard) .rt-team-table__body {
    display: grid;
    gap: .75rem;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: .65rem;
    min-height: 0;
    padding: 1rem;
    border: 1px solid rgba(6,17,32,.10);
    border-radius: 16px;
    background: #fff;
    box-shadow: 0 10px 22px rgba(6,17,32,.055);
  }

  body:has(.rt-team-central--dashboard) .rt-team-row > div {
    display: grid;
    grid-template-columns: 96px minmax(0,1fr);
    align-items: center;
    gap: .75rem;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row > div::before {
    content: attr(data-label);
    color: #6b7280;
    font-size: .64rem;
    font-weight: 900;
    letter-spacing: .12em;
    text-transform: uppercase;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach {
    display: grid;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach > img,
  body:has(.rt-team-central--dashboard) .rt-team-row__coach > span {
    grid-column: 2;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach {
    grid-template-columns: 96px 44px minmax(0,1fr);
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach::before {
    grid-column: 1;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach > img {
    grid-column: 2;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach > span {
    grid-column: 3;
  }
}

@media (max-width: 520px) {
  body:has(.rt-team-central--dashboard) .rt-season-dashboard {
    border-radius: 16px;
  }

  body:has(.rt-team-central--dashboard) .rt-season-dashboard__top,
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary,
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__terms {
    padding: 1rem;
  }

  body:has(.rt-team-central--dashboard) .rt-team-row > div {
    grid-template-columns: 82px minmax(0,1fr);
  }

  body:has(.rt-team-central--dashboard) .rt-team-row__coach {
    grid-template-columns: 82px 42px minmax(0,1fr);
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
    print("Appended Team Central unified season dashboard CSS to assets/css/main.css")
else:
    print("Team Central unified season dashboard CSS already present; no changes made.")
