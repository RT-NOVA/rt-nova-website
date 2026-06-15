#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit("Missing assets/css/main.css")

css = css_path.read_text()
marker = "/* Team Central combined selector/season header */"
if marker not in css:
    css += r'''

/* Team Central combined selector/season header */
body:has(.rt-team-central--dashboard) .rt-season-dashboard {
  overflow: hidden !important;
  border-radius: 22px !important;
  border: 1px solid rgba(6, 17, 32, .12) !important;
  background: #fff !important;
  box-shadow: 0 22px 52px rgba(6, 17, 32, .10) !important;
}

/* Treat the white selector and dark season summary as one connected component. */
body:has(.rt-team-central--dashboard) .rt-season-dashboard__top,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle {
  margin: 0 !important;
  border: 0 !important;
  border-bottom: 4px solid var(--rt-orange, #f15a24) !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  background: #fff !important;
  padding: clamp(1rem, 2.1vw, 1.45rem) clamp(1.1rem, 2.8vw, 2rem) !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__selector-copy h3,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__top h3 {
  margin: 0 !important;
  font-size: clamp(2rem, 4vw, 3.2rem) !important;
  line-height: .95 !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__selector-copy p,
body:has(.rt-team-central--dashboard) .rt-season-dashboard__top p {
  margin-top: .45rem !important;
  margin-bottom: 0 !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary {
  margin: 0 !important;
  border: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  background: #07111f !important;
  padding: clamp(1.25rem, 2.7vw, 2rem) clamp(1.1rem, 2.8vw, 2rem) !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary > div {
  max-width: none !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary h2 {
  margin: 0 0 .35rem !important;
  font-size: clamp(2.6rem, 5.2vw, 4.3rem) !important;
  line-height: .9 !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary p {
  margin: 0 !important;
}

/* If the older right-side summary text still exists, hide it so the dark band is clean. */
body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary > p {
  display: none !important;
}

body:has(.rt-team-central--dashboard) .rt-season-dashboard__terms {
  margin: 0 !important;
  border-top: 0 !important;
  padding-top: clamp(1rem, 2.2vw, 1.55rem) !important;
}

/* Mobile: keep the selector, toggle, and season title connected but stacked. */
@media (max-width: 760px) {
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__top,
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__top--toggle {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
    align-items: start !important;
  }

  body:has(.rt-team-central--dashboard) .rt-season-toggle,
  body:has(.rt-team-central--dashboard) .rt-season-segmented,
  body:has(.rt-team-central--dashboard) .rt-season-dashboard__toggle {
    width: 100% !important;
  }

  body:has(.rt-team-central--dashboard) .rt-season-dashboard__summary {
    display: block !important;
  }
}
'''
    css_path.write_text(css)

print("Applied Team Central combined selector/season header CSS.")
print("Updated: assets/css/main.css")
