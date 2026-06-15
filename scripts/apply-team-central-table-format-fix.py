#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-team-table-format-fix")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central clean table format fix */"
append = r'''

/* Team Central clean table format fix */
body:has(.rt-team-central--clean-table) .rt-season-dashboard__summary--clean {
  display: block;
}

body:has(.rt-team-central--clean-table) .rt-season-dashboard__summary--clean h2 {
  margin: 0 0 .25rem;
}

body:has(.rt-team-central--clean-table) .rt-season-dashboard__summary--clean p {
  margin: 0;
}

body:has(.rt-team-central--clean-table) .rt-season-dashboard__summary--clean .rt-badge,
body:has(.rt-team-central--clean-table) .rt-team-term__head .rt-badge,
body:has(.rt-team-central--clean-table) .rt-team-row__status,
body:has(.rt-team-central--clean-table) .rt-team-table__status,
body:has(.rt-team-central--clean-table) .rt-badge--active,
body:has(.rt-team-central--clean-table) .rt-badge--past,
body:has(.rt-team-central--clean-table) .rt-badge--upcoming,
body:has(.rt-team-central--clean-table) .rt-badge--current,
body:has(.rt-team-central--clean-table) .rt-badge--coming-soon,
body:has(.rt-team-central--clean-table) .rt-badge--comingsoon {
  display: none !important;
}

body:has(.rt-team-central--clean-table) .rt-team-term__head--clean {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: .75rem;
  padding-bottom: .7rem;
  border-bottom: 1px solid rgba(6,17,32,.10);
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean {
  overflow: hidden;
  border: 1px solid rgba(6,17,32,.10);
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 18px 34px rgba(6,17,32,.08);
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-table__head,
body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row {
  display: grid !important;
  grid-template-columns: minmax(120px, .75fr) minmax(260px, 1.45fr) minmax(80px, .45fr) minmax(320px, 1.65fr) !important;
  align-items: center;
  column-gap: 1.2rem;
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-table__head {
  padding: .72rem 1rem;
  background: #f3f4f6;
  border-bottom: 1px solid rgba(6,17,32,.11);
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-table__head span {
  color: #4b5563;
  font-size: .66rem;
  font-weight: 950;
  letter-spacing: .16em;
  text-transform: uppercase;
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row {
  padding: .75rem 1rem;
  border-bottom: 1px solid rgba(6,17,32,.07);
  background: #fff;
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row:nth-child(even) {
  background: #f7f8fb;
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row:last-child {
  border-bottom: 0;
}

body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row:hover {
  background: #fff7f1;
}

body:has(.rt-team-central--clean-table) .rt-team-row__team strong,
body:has(.rt-team-central--clean-table) .rt-team-row__record strong {
  color: #07111f;
  font-weight: 950;
}

body:has(.rt-team-central--clean-table) .rt-team-row__coach {
  display: flex;
  align-items: center;
  gap: .7rem;
}

body:has(.rt-team-central--clean-table) .rt-team-row__coach img {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  object-fit: cover;
  box-shadow: 0 10px 18px rgba(6,17,32,.14);
}

body:has(.rt-team-central--clean-table) .rt-team-row__coach small {
  display: block;
  color: #b94f2a;
  font-size: .64rem;
  font-weight: 950;
  letter-spacing: .11em;
  line-height: 1.1;
  text-transform: uppercase;
}

body:has(.rt-team-central--clean-table) .rt-team-row__coach strong {
  display: block;
  color: #07111f;
  font-size: .9rem;
  font-weight: 950;
  letter-spacing: .04em;
  line-height: 1.2;
  text-transform: uppercase;
}

body:has(.rt-team-central--clean-table) .rt-team-row__links {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: .38rem;
}

body:has(.rt-team-central--clean-table) .rt-team-row__links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 26px;
  padding: .36rem .68rem;
  border: 1px solid rgba(6,17,32,.12);
  border-radius: 999px;
  background: #fff;
  color: #07111f;
  font-size: .64rem;
  font-weight: 950;
  letter-spacing: .10em;
  line-height: 1;
  text-decoration: none;
  text-transform: uppercase;
}

body:has(.rt-team-central--clean-table) .rt-team-row__links a:hover {
  border-color: #f15a24;
  background: #f15a24;
  color: #fff;
}

body:has(.rt-team-central--clean-table) .rt-season-dashboard__terms--clean {
  display: grid;
  gap: clamp(1.25rem, 2.2vw, 1.9rem);
}

@media (max-width: 860px) {
  body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-table__head {
    display: none !important;
  }

  body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: .7rem;
    padding: 1rem;
  }

  body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row > div {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: .75rem;
    align-items: center;
  }

  body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row > div::before {
    content: attr(data-label);
    color: #6b7280;
    font-size: .62rem;
    font-weight: 950;
    letter-spacing: .12em;
    text-transform: uppercase;
  }

  body:has(.rt-team-central--clean-table) .rt-team-row__links {
    align-items: start;
  }
}

@media (max-width: 520px) {
  body:has(.rt-team-central--clean-table) .rt-team-table--clean .rt-team-row > div {
    grid-template-columns: 1fr;
    gap: .35rem;
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
    print("Appended Team Central clean table format fix CSS.")
else:
    print("Team Central clean table format fix CSS already present.")
