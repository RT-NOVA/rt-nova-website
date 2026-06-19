#!/usr/bin/env python3
from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(".")
CSS_DIR = ROOT / "assets" / "css"

if not CSS_DIR.exists():
    raise SystemExit("Missing assets/css directory. Run this from the repo root.")

AUDIT_PATTERNS = [
    "rt-navy",
    "rt-navy-2",
    "#061120",
    "#0c1b2e",
    "#07101f",
    "#07111f",
    "#080f1b",
    "#0f172a",
    "#111827",
    "#1f2937",
    "rgba(6,17,32",
    "rgba(6, 17, 32",
    "rgba(3,10,20",
    "rgba(3, 10, 20",
    "rgba(8,15,27",
    "rgba(8, 15, 27",
    "rgba(7,16,31",
    "rgba(7, 16, 31",
]

served_css_files = [
    p for p in CSS_DIR.glob("*.css")
    if ".bak" not in p.name and not p.name.endswith(".map")
]

print("Scanning served CSS files:")
for p in served_css_files:
    print(f"  - {p}")

before_hits = defaultdict(list)
for p in served_css_files:
    text = p.read_text(errors="ignore")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if any(token.lower() in line.lower() for token in AUDIT_PATTERNS):
            before_hits[str(p)].append((lineno, line.strip()))

def replace_rgba_family(text, r, g, b, new="5,5,5"):
    # Handles rgba(6,17,32,.14) and rgba(6, 17, 32, .14)
    pattern = rf"rgba\(\s*{r}\s*,\s*{g}\s*,\s*{b}\s*,"
    return re.sub(pattern, f"rgba({new},", text)

for p in served_css_files:
    text = p.read_text(errors="ignore")
    original = text

    # Normalize the site dark variables.
    text = re.sub(r"--rt-navy\s*:\s*#[0-9a-fA-F]{3,6}\s*;", "--rt-navy:#0b0b0d;", text, count=1)
    text = re.sub(r"--rt-navy-2\s*:\s*#[0-9a-fA-F]{3,6}\s*;", "--rt-navy-2:#151515;", text, count=1)

    # Replace direct navy/slate hexes in served CSS files.
    replacements = {
        "#061120": "#0b0b0d",
        "#0c1b2e": "#151515",
        "#07101f": "#0b0b0d",
        "#07111f": "#0b0b0d",
        "#080f1b": "#0b0b0d",
        "#0b1220": "#111111",
        "#101828": "#151515",
        "#0f172a": "#151515",
        "#111827": "#151515",
        "#1f2937": "#1a1a1a",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
        text = text.replace(old.upper(), new)

    # Replace blue-toned rgba shadows/overlays with neutral black/charcoal equivalents.
    for rgb in [(6,17,32), (3,10,20), (8,15,27), (7,16,31), (12,27,46)]:
        text = replace_rgba_family(text, *rgb, new="5,5,5")

    if p.name == "main.css":
        start = "/* RT NOVA navy cleanup final pass */"
        end = "/* End RT NOVA navy cleanup final pass */"
        text = re.sub(
            rf"\n?{re.escape(start)}[\s\S]*?{re.escape(end)}\n?",
            "\n",
            text,
        )

        final_block = r'''
/* RT NOVA navy cleanup final pass */
:root {
  --rt-black:#050505;
  --rt-charcoal:#0b0b0d;
  --rt-charcoal-2:#151515;
  --rt-navy:#0b0b0d;
  --rt-navy-2:#151515;
  --rt-ink:#151515;
  --rt-shadow:0 18px 45px rgba(5,5,5,.14);
  --rt-shadow-soft:0 10px 25px rgba(5,5,5,.08);
}

/* Global dark surfaces */
.site-utility,
.site-footer,
.program-strip,
.rt-section--dark,
.rt-info-card--dark,
.rt-feature-card--dark,
.rt-team-season-summary,
.rt-team-season-nav,
.rt-card--dark,
.rt-panel--dark,
.rt-band--dark {
  background:
    radial-gradient(circle at 18% 0%, rgba(245,91,32,.11), transparent 30%),
    linear-gradient(135deg, #050505 0%, #0b0b0d 62%, #151515 100%) !important;
  color:#fff;
}

/* Header remains crisp black. */
.site-header--twelve,
.site-header--twelve .site-header__bar,
.site-header--twelve .site-nav--twelve,
.rt-site-header,
.site-header__bar {
  background:#050505 !important;
}

/* Page heroes: charcoal-black, not navy. */
.rt-page-hero,
.page-hero,
.hero,
.rt-hero {
  background:
    radial-gradient(circle at 18% 30%, rgba(245,91,32,.16), transparent 31%),
    linear-gradient(135deg, #050505 0%, #0b0b0d 56%, #171717 100%) !important;
  border-bottom:1px solid rgba(245,91,32,.18);
  color:#fff;
}

/* Home hero overlay: remove the blue cast. */
.home-hero {
  background:#050505 !important;
}

.home-hero::before {
  background:
    radial-gradient(circle at 14% 45%, rgba(245,91,32,.16), transparent 30%),
    linear-gradient(90deg, rgba(0,0,0,.95) 0%, rgba(8,8,8,.82) 45%, rgba(8,8,8,.34) 100%),
    linear-gradient(0deg, rgba(0,0,0,.74), rgba(0,0,0,.08) 48%, rgba(0,0,0,.28)) !important;
}

/* Booster/Sponsorship contact and CTA sections were the most likely to keep navy. */
.rt-booster-contact,
.rt-booster-contact-section,
.rt-booster-cta,
.booster-contact,
.booster-contact-section,
.booster-cta,
.sponsor-contact,
.sponsor-contact-section,
.sponsor-cta,
.rt-contact-band,
.rt-final-cta,
.rt-page-cta {
  background:
    radial-gradient(circle at 12% 0%, rgba(245,91,32,.12), transparent 32%),
    linear-gradient(135deg, #050505 0%, #0b0b0d 60%, #151515 100%) !important;
  color:#fff;
}

/* Tables and dark table headers. */
.sponsor-benefits-table thead th,
.rt-table thead th,
.rt-table__head,
.rt-tryout-card__head {
  background:#0b0b0d !important;
  color:#fff;
}

/* Keep text dark but neutral, not blue. */
h1, h2, h3,
.section-intro h2,
.rt-section-heading h2,
.rt-page-hero__card,
.rt-page-hero__card strong,
.rt-team-proof-strip .rt-proof-grid strong,
.rt-roster-proof-strip .rt-proof-grid strong,
.proof-band strong,
.feature-list strong,
.image-card__body h3 {
  color:var(--rt-navy);
}

/* Buttons using dark outlines should now use charcoal/black. */
.rt-btn--light,
.rt-btn-outline-dark,
.rt-btn--dark-outline {
  color:var(--rt-navy);
  border-color:var(--rt-navy);
}

.rt-btn-outline-dark:hover,
.rt-btn-outline-dark:focus-visible,
.rt-btn--dark-outline:hover,
.rt-btn--dark-outline:focus-visible {
  background:var(--rt-navy);
  color:#fff;
}

/* Social Hub placeholder/card dark pieces. */
.social-feed-card__avatar,
.social-feed-card__image--placeholder,
.social-hub__button:not(.social-hub__button--outline) {
  background:#0b0b0d !important;
  border-color:#0b0b0d !important;
}

@media (max-width:720px) {
  .home-hero::before {
    background:
      radial-gradient(circle at 10% 75%, rgba(245,91,32,.14), transparent 34%),
      linear-gradient(0deg, rgba(0,0,0,.94) 0%, rgba(0,0,0,.62) 55%, rgba(0,0,0,.2) 100%) !important;
  }
}
/* End RT NOVA navy cleanup final pass */
'''
        text = text.rstrip() + "\n\n" + final_block.strip() + "\n"

    if text != original:
        p.write_text(text)
        print(f"Updated {p}")
    else:
        print(f"No changes needed in {p}")

after_hits = defaultdict(list)
for p in served_css_files:
    text = p.read_text(errors="ignore")
    for lineno, line in enumerate(text.splitlines(), start=1):
        # Only report hard-coded old navy values and blue rgba families after replacement.
        if any(token.lower() in line.lower() for token in [
            "#061120", "#0c1b2e", "#07101f", "#07111f", "#080f1b", "#0f172a",
            "rgba(6,17,32", "rgba(6, 17, 32", "rgba(3,10,20", "rgba(3, 10, 20",
            "rgba(8,15,27", "rgba(8, 15, 27", "rgba(7,16,31", "rgba(7, 16, 31"
        ]):
            after_hits[str(p)].append((lineno, line.strip()))

report_path = Path("NAVY_CLEANUP_AUDIT.md")
lines = []
lines.append("# Navy Cleanup Audit\n")
lines.append("This report was generated by `scripts/apply-navy-cleanup-final-pass.py`.\n")
lines.append("## Served CSS files scanned\n")
for p in served_css_files:
    lines.append(f"- `{p}`")
lines.append("\n## Remaining hard-coded old navy/blue values after cleanup\n")
if after_hits:
    for file, hits in after_hits.items():
        lines.append(f"\n### `{file}`")
        for lineno, line in hits[:80]:
            lines.append(f"- L{lineno}: `{line}`")
        if len(hits) > 80:
            lines.append(f"- ... {len(hits)-80} more")
else:
    lines.append("No remaining hard-coded old navy/blue hex or rgba values were found in served CSS files.")
lines.append("\n## Notes\n")
lines.append("- `var(--rt-navy)` may still appear in CSS, but it now resolves to near-black `#0b0b0d`.")
lines.append("- Backup files such as `*.bak*` are intentionally not modified because Hugo should not serve them as active CSS.")
report_path.write_text("\n".join(lines) + "\n")

print(f"Wrote {report_path}")

if after_hits:
    print("\nRemaining old navy/blue values were found. See NAVY_CLEANUP_AUDIT.md")
else:
    print("\nNo remaining hard-coded old navy/blue values found in served CSS files.")
print("Run: hugo server -D --disableFastRender")
