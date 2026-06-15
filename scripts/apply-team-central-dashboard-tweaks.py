#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-team-dashboard-tweaks")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central dashboard selector + banded table tweaks */"
append = r'''

/* Team Central dashboard selector + banded table tweaks */
body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle {
  align-items: center;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle h3 {
  margin-bottom: 0;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle p {
  display: none !important;
}

body:has(.rt-team-central--dashboard) .rt-season-toggle {
  display: inline-grid;
  grid-template-columns: repeat(2, minmax(130px, 1fr));
  gap: .25rem;
  justify-self: end;
  width: min(100%, 430px);
  padding: .28rem;
  border: 1px solid rgba(6,17,32,.12);
  border-radius: 999px;
  background: #f3f4f6;
  box-shadow: inset 0 1px 2px rgba(6,17,32,.06);
}

body:has(.rt-team-central--dashboard) .rt-season-toggle__button {
  display: grid;
  gap: .08rem;
  min-height: 42px;
  padding: .55rem .85rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: #4b5563;
  cursor: pointer;
  text-align: center;
}

body:has(.rt-team-central--dashboard) .rt-season-toggle__button span {
  font-size: .58rem;
  font-weight: 900;
  letter-spacing: .16em;
  line-height: 1;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-season-toggle__button strong {
  color: inherit;
  font-size: .82rem;
  font-weight: 950;
  line-height: 1;
  letter-spacing: .04em;
  text-transform: uppercase;
}

body:has(.rt-team-central--dashboard) .rt-season-toggle__button[aria-selected="true"],
body:has(.rt-team-central--dashboard) .rt-season-toggle__button.is-active {
  background: #07111f;
  color: #fff;
  box-shadow: 0 8px 20px rgba(6,17,32,.18);
}

body:has(.rt-team-central--dashboard) .rt-season-toggle__button:not([aria-selected="true"]):hover {
  background: rgba(255,255,255,.72);
  color: #07111f;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary--simple {
  display: block;
  padding-top: clamp(1rem, 2vw, 1.35rem);
  padding-bottom: clamp(1rem, 2vw, 1.35rem);
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary--simple > div {
  display: grid;
  gap: .18rem;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary--simple h2 {
  margin: .25rem 0 .15rem;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary .rt-badge--upcoming,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary .rt-badge--coming-soon,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary .rt-badge--comingsoon {
  background: #f15a24 !important;
  border-color: #f15a24 !important;
  color: #fff !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary .rt-badge--current,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary .rt-badge--active {
  background: #fff4ec !important;
  border-color: #fff4ec !important;
  color: #a94724 !important;
}

body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row {
  background: #fff;
}

body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row:nth-child(even) {
  background: #f7f8fb;
}

body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row:nth-child(odd) {
  background: #fff;
}

body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row:hover {
  background: #fff7f1;
}

@media (max-width: 860px) {
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle {
    grid-template-columns: 1fr;
  }

  body:has(.rt-team-central--dashboard) .rt-season-toggle {
    justify-self: stretch;
    width: 100%;
  }

  body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row:nth-child(even),
  body:has(.rt-team-central--dashboard) .rt-team-table__body .rt-team-row:nth-child(odd) {
    background: #fff;
  }
}

@media (max-width: 460px) {
  body:has(.rt-team-central--dashboard) .rt-season-toggle {
    grid-template-columns: 1fr;
    border-radius: 18px;
  }

  body:has(.rt-team-central--dashboard) .rt-season-toggle__button {
    border-radius: 14px;
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
    print("Appended Team Central dashboard selector + banded table CSS to assets/css/main.css")
else:
    print("Team Central dashboard selector + banded table CSS already present; no changes made.")
