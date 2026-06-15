#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-team-table-layout")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central themed table layout */"
append = r'''

/* Team Central themed table layout */
body:has(.rt-team-central--table) .rt-page-hero__card {
  display: none !important;
}
body:has(.rt-team-central--table) .rt-page-hero__inner {
  grid-template-columns: minmax(0, 860px) !important;
}

.rt-team-central--table {
  background: var(--rt-cream, #f5f1ea);
}
.rt-team-central__intro {
  max-width: 920px;
  text-align: center;
  margin-bottom: clamp(1.25rem, 3vw, 2rem);
}
.rt-team-central__intro h2 {
  margin: .2rem 0 .6rem;
  font-size: clamp(3rem, 7vw, 5.4rem);
  line-height: .92;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.rt-team-central__intro p {
  color: var(--rt-muted);
  font-weight: 700;
}
.rt-season-helper {
  margin-top: .35rem !important;
  color: var(--rt-muted);
  font-size: .98rem;
  line-height: 1.45;
  font-weight: 700;
}

.rt-season-selector-card--compact {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 460px);
  gap: clamp(1rem, 3vw, 2rem);
  align-items: end;
  padding: clamp(1.15rem, 3vw, 1.65rem);
  background: #fff;
  border: 1px solid rgba(6,17,32,.09);
  border-bottom: 4px solid var(--rt-orange);
  border-radius: 18px;
  box-shadow: 0 18px 42px rgba(6,17,32,.08);
}
.rt-season-selector-card--compact h3 {
  margin: .15rem 0 0;
  font-size: clamp(2rem, 4.8vw, 3.15rem);
  line-height: .95;
  letter-spacing: .06em;
  text-transform: uppercase;
}
.rt-season-selector-card--compact p {
  margin: .45rem 0 0;
}
.rt-season-select-label {
  display: grid;
  gap: .35rem;
}
.rt-season-select-label span {
  color: var(--rt-orange-dark);
  font-size: .72rem;
  font-weight: 950;
  letter-spacing: .14em;
  text-transform: uppercase;
}
.rt-season-select {
  width: 100%;
  min-height: 44px;
  border: 1px solid rgba(6,17,32,.18);
  border-radius: 999px;
  padding: .65rem 1rem;
  background: #fff;
  color: var(--rt-navy);
  font-weight: 850;
}

.rt-season-panel[hidden] {
  display: none;
}
.rt-season-panel__head--table {
  display: grid;
  grid-template-columns: minmax(260px, .9fr) minmax(0, 1fr);
  gap: clamp(1rem, 4vw, 3rem);
  align-items: center;
  margin: clamp(1.15rem, 3vw, 2rem) 0 clamp(1rem, 3vw, 1.5rem);
  padding: clamp(1.4rem, 4vw, 2.2rem);
  background: var(--rt-navy);
  color: #fff;
  border-bottom: 4px solid var(--rt-orange);
  border-radius: 18px;
  box-shadow: 0 18px 42px rgba(6,17,32,.16);
}
.rt-season-panel__head--table h2 {
  margin: .55rem 0 .15rem;
  color: #fff;
  font-size: clamp(3rem, 7vw, 5rem);
  line-height: .9;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.rt-season-panel__head--table p {
  margin: 0;
  color: rgba(255,255,255,.78);
  font-weight: 750;
  line-height: 1.45;
}
.rt-season-panel__head--table > p {
  max-width: 620px;
  justify-self: end;
}

.rt-team-term--table {
  margin: clamp(1.25rem, 3vw, 2rem) 0;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.rt-team-term__head--table {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  padding-bottom: .85rem;
  border-bottom: 1px solid rgba(6,17,32,.12);
}
.rt-team-term__head--table h3 {
  margin: .15rem 0 0;
  font-size: clamp(2.1rem, 5vw, 3.35rem);
  line-height: .92;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.rt-team-table {
  overflow: hidden;
  margin-top: 1rem;
  background: #fff;
  border: 1px solid rgba(6,17,32,.09);
  border-radius: 18px;
  box-shadow: 0 18px 42px rgba(6,17,32,.08);
}
.rt-team-table__head,
.rt-team-row {
  display: grid;
  grid-template-columns: 130px minmax(110px, .75fr) minmax(240px, 1.2fr) 110px minmax(260px, 1.25fr);
  gap: 1rem;
  align-items: center;
}
.rt-team-table__head {
  min-height: 48px;
  padding: 0 1rem;
  background: #f2f3f5;
  color: #4f5563;
  border-bottom: 1px solid rgba(6,17,32,.11);
  font-size: .72rem;
  font-weight: 950;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.rt-team-row {
  min-height: 86px;
  padding: .75rem 1rem;
  border-bottom: 1px solid rgba(6,17,32,.08);
}
.rt-team-row:last-child {
  border-bottom: 0;
}
.rt-team-row__team strong,
.rt-team-row__record strong {
  color: var(--rt-navy);
  font-weight: 950;
}
.rt-team-row__team strong {
  font-size: 1.12rem;
}
.rt-team-row__coach {
  display: flex;
  align-items: center;
  gap: .85rem;
}
.rt-team-row__coach img {
  width: 54px;
  height: 54px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 0 0 1px rgba(6,17,32,.12), 0 8px 18px rgba(6,17,32,.14);
}
.rt-team-row__coach small {
  display: block;
  margin-bottom: .15rem;
  color: var(--rt-orange-dark);
  font-size: .68rem;
  font-weight: 950;
  letter-spacing: .08em;
  line-height: 1;
  text-transform: uppercase;
}
.rt-team-row__coach strong {
  display: block;
  color: var(--rt-navy);
  font-size: .95rem;
  line-height: 1.12;
  text-transform: uppercase;
}
.rt-team-row__links {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  align-items: center;
}
.rt-team-row__links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 32px;
  padding: .45rem .72rem;
  border: 1px solid rgba(6,17,32,.13);
  border-radius: 999px;
  background: #fff;
  color: var(--rt-navy);
  font-size: .68rem;
  font-weight: 950;
  letter-spacing: .06em;
  line-height: 1;
  text-transform: uppercase;
  text-decoration: none;
}
.rt-team-row__links a:hover {
  background: var(--rt-orange);
  border-color: var(--rt-orange);
  color: #fff;
}
.rt-team-row__links .rt-muted {
  color: var(--rt-muted);
  font-size: .94rem;
  font-weight: 700;
}

.rt-empty-team-note--table {
  margin-top: 1rem;
  padding: clamp(1rem, 2.5vw, 1.25rem);
  border: 1px solid rgba(6,17,32,.08);
  border-radius: 18px;
  background: rgba(255,255,255,.72);
  box-shadow: 0 14px 32px rgba(6,17,32,.06);
}
.rt-empty-team-note--table strong,
.rt-empty-team-note--table span {
  display: block;
}
.rt-empty-team-note--table span {
  margin-top: .25rem;
  color: var(--rt-muted);
  font-weight: 700;
}

.rt-team-archive--compact {
  padding-top: 0 !important;
}
.rt-archive-compact {
  overflow: hidden;
  background: #fff;
  border: 1px solid rgba(6,17,32,.09);
  border-radius: 18px;
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
  letter-spacing: .14em;
  text-transform: uppercase;
}
.rt-archive-compact summary strong {
  color: var(--rt-navy);
  font-family: var(--rt-display);
  font-size: clamp(1.35rem, 2.3vw, 1.8rem);
  line-height: 1;
  letter-spacing: .06em;
  text-transform: uppercase;
}
.rt-archive-compact__list {
  display: grid;
  gap: .65rem;
  padding: 0 clamp(1rem, 2.5vw, 1.35rem) clamp(1rem, 2.5vw, 1.35rem);
}
.rt-archive-compact__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .75rem .85rem;
  background: #f8f8f8;
  border: 1px solid rgba(6,17,32,.08);
  border-radius: 12px;
}
.rt-archive-compact__item strong {
  color: var(--rt-navy);
}
.rt-archive-compact__item span {
  color: var(--rt-muted);
  font-weight: 700;
}

@media (max-width: 1080px) {
  .rt-team-table__head,
  .rt-team-row {
    grid-template-columns: 105px minmax(90px,.65fr) minmax(220px,1.15fr) 90px minmax(190px,1fr);
  }
}
@media (max-width: 820px) {
  .rt-season-selector-card--compact,
  .rt-season-panel__head--table {
    grid-template-columns: 1fr;
  }
  .rt-season-panel__head--table > p {
    justify-self: start;
  }
  .rt-team-table {
    background: transparent;
    border: 0;
    border-radius: 0;
    box-shadow: none;
  }
  .rt-team-table__head {
    display: none;
  }
  .rt-team-table__body {
    display: grid;
    gap: .9rem;
  }
  .rt-team-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: .7rem;
    min-height: 0;
    padding: 1rem;
    background: #fff;
    border: 1px solid rgba(6,17,32,.09);
    border-radius: 16px;
    box-shadow: 0 14px 30px rgba(6,17,32,.07);
  }
  .rt-team-row__status,
  .rt-team-row__team,
  .rt-team-row__coach,
  .rt-team-row__record,
  .rt-team-row__links {
    position: relative;
  }
  .rt-team-row__team strong {
    font-size: 1.45rem;
  }
  .rt-team-row__record::before {
    content: "Record: ";
    color: var(--rt-muted);
    font-weight: 800;
  }
}
@media (max-width: 520px) {
  .rt-team-central__intro h2,
  .rt-season-panel__head--table h2,
  .rt-team-term__head--table h3 {
    letter-spacing: .05em;
  }
  .rt-team-term__head--table,
  .rt-archive-compact summary span,
  .rt-archive-compact__item {
    align-items: flex-start;
    flex-direction: column;
  }
  .rt-team-row__links a {
    min-height: 34px;
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
else:
    print("Team Central themed table CSS already present; no CSS appended.")
