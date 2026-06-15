#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
css_path = root / "assets" / "css" / "main.css"
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

bak = css_path.with_suffix(css_path.suffix + ".bak-teamcentral-final-cleanup")
if not bak.exists():
    bak.write_text(css_path.read_text())

css = css_path.read_text()
marker = "/* Team Central final dashboard cleanup */"
append = r'''

/* Team Central final dashboard cleanup */
body:has(.rt-team-central--final-cleanup) .rt-team-central__intro .rt-eyebrow,
body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__top .rt-eyebrow,
body:has(.rt-team-central--final-cleanup) .rt-team-term__head .rt-eyebrow,
body:has(.rt-team-central--final-cleanup) .rt-team-term__kicker,
body:has(.rt-team-central--final-cleanup) .team-term__kicker,
body:has(.rt-team-central--final-cleanup) .team-central-term__kicker {
  display: none !important;
}

body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__top--clean {
  padding-top: clamp(1.25rem, 2vw, 1.75rem) !important;
  padding-bottom: clamp(1.1rem, 1.8vw, 1.55rem) !important;
}

body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__top--clean h3 {
  margin: 0 !important;
}

body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__summary--clean {
  padding-top: clamp(1.45rem, 2.8vw, 2.1rem) !important;
  padding-bottom: clamp(1.3rem, 2.3vw, 1.8rem) !important;
}

body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__terms--clean {
  gap: clamp(1rem, 1.8vw, 1.45rem) !important;
  padding-top: clamp(1.35rem, 2.2vw, 1.8rem) !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-term {
  margin: 0 !important;
  padding: 0 !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-term + .rt-team-term {
  margin-top: clamp(.9rem, 1.6vw, 1.35rem) !important;
  padding-top: clamp(.9rem, 1.5vw, 1.25rem) !important;
  border-top: 1px solid rgba(6, 17, 32, .10);
}

body:has(.rt-team-central--final-cleanup) .rt-team-term__head--clean {
  margin-bottom: .55rem !important;
  padding-bottom: .48rem !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-term__head--clean h3 {
  margin: 0 !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-table--clean .rt-team-table__head {
  padding-top: .58rem !important;
  padding-bottom: .58rem !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-table--clean .rt-team-row {
  padding-top: .58rem !important;
  padding-bottom: .58rem !important;
}

body:has(.rt-team-central--final-cleanup) .rt-team-row__coach img {
  width: 38px !important;
  height: 38px !important;
}

body:has(.rt-team-central--final-cleanup) .rt-empty-team-note--dashboard {
  margin-top: .45rem !important;
  padding: .9rem 1rem !important;
}

body:has(.rt-team-central--final-cleanup) .rt-empty-team-note--dashboard a {
  color: #f15a24;
  font-weight: 900;
  text-decoration: underline;
  text-underline-offset: .18em;
}

body:has(.rt-team-central--final-cleanup) .rt-team-archive,
body:has(.rt-team-central--final-cleanup) .team-archive,
body:has(.rt-team-central--final-cleanup) .team-central-archive,
body:has(.rt-team-central--final-cleanup) .rt-team-past-seasons,
body:has(.rt-team-central--final-cleanup) .team-past-seasons,
body:has(.rt-team-central--final-cleanup) .past-seasons,
body:has(.rt-team-central--final-cleanup) details.team-archive,
body:has(.rt-team-central--final-cleanup) details.rt-team-archive {
  display: none !important;
}

@media (max-width: 860px) {
  body:has(.rt-team-central--final-cleanup) .rt-season-dashboard__terms--clean {
    padding-top: 1rem !important;
  }

  body:has(.rt-team-central--final-cleanup) .rt-team-table--clean .rt-team-row {
    padding: .9rem !important;
  }
}
'''

if marker not in css:
    css_path.write_text(css.rstrip() + append + "\n")
    print("Appended Team Central final cleanup CSS.")
else:
    print("Team Central final cleanup CSS already present; no CSS changes made.")
