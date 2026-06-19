#!/usr/bin/env python3
from pathlib import Path
import re

css_path = Path("assets/css/main.css")
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

css = css_path.read_text()

start = "/* RT NOVA brand black/orange theme refresh */"
end = "/* End RT NOVA brand black/orange theme refresh */"

css = re.sub(
    rf"\n?{re.escape(start)}[\s\S]*?{re.escape(end)}\n?",
    "\n",
    css,
)

# Update the global dark variables from navy to near-black/charcoal.
css = re.sub(r"--rt-navy\s*:\s*#[0-9a-fA-F]{3,6}\s*;", "--rt-navy:#0b0b0d;", css, count=1)
css = re.sub(r"--rt-navy-2\s*:\s*#[0-9a-fA-F]{3,6}\s*;", "--rt-navy-2:#151515;", css, count=1)

theme_block = r'''
/* RT NOVA brand black/orange theme refresh */
:root {
  --rt-black:#050505;
  --rt-charcoal:#0b0b0d;
  --rt-charcoal-2:#151515;
  --rt-navy:#0b0b0d;
  --rt-navy-2:#151515;
}

/* Header stays crisp black, while heroes use warmer charcoal layers. */
.site-header--twelve,
.site-header--twelve .site-header__bar,
.site-header--twelve .site-nav--twelve {
  background:var(--rt-black);
}

/* Generic page heroes: replace navy with Rawlings-style black/charcoal + subtle orange energy. */
.rt-page-hero {
  background:
    radial-gradient(circle at 18% 30%, rgba(245, 91, 32, .16), transparent 31%),
    linear-gradient(135deg, #050505 0%, #0b0b0d 56%, #171717 100%);
  border-bottom:1px solid rgba(245, 91, 32, .18);
}

/* Homepage hero overlay: keep image support, but remove the blue cast. */
.home-hero {
  background:#050505;
}

.home-hero::before {
  background:
    radial-gradient(circle at 14% 45%, rgba(245, 91, 32, .16), transparent 30%),
    linear-gradient(90deg, rgba(0,0,0,.95) 0%, rgba(8,8,8,.82) 45%, rgba(8,8,8,.34) 100%),
    linear-gradient(0deg, rgba(0,0,0,.74), rgba(0,0,0,.08) 48%, rgba(0,0,0,.28));
}

/* Dark support bands should match the brand system instead of using blue navy. */
.rt-section--dark,
.program-strip,
.site-footer,
.rt-proof-strip:not(.rt-proof-strip--light) {
  background:
    radial-gradient(circle at 18% 0%, rgba(245, 91, 32, .11), transparent 30%),
    linear-gradient(135deg, #050505 0%, #0b0b0d 62%, #151515 100%);
}

/* Smaller dark cards/headers. */
.rt-tryout-card__head {
  background:
    linear-gradient(135deg, #050505 0%, #111 100%);
}

/* Keep ghost button hover readable after the dark color shift. */
.rt-btn--ghost:hover,
.rt-btn-outline:hover {
  color:var(--rt-black);
}

/* Mobile homepage hero overlay also uses black instead of navy. */
@media (max-width:720px) {
  .home-hero::before {
    background:
      radial-gradient(circle at 10% 75%, rgba(245, 91, 32, .14), transparent 34%),
      linear-gradient(0deg, rgba(0,0,0,.94) 0%, rgba(0,0,0,.62) 55%, rgba(0,0,0,.2) 100%);
  }
}
/* End RT NOVA brand black/orange theme refresh */
'''

css = css.rstrip() + "\n\n" + theme_block.strip() + "\n"

css_path.write_text(css)
print("Updated assets/css/main.css with black/charcoal + orange brand theme overrides.")
print("Run: hugo server -D --disableFastRender")
