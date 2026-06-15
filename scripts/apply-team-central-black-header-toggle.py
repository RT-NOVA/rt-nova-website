#!/usr/bin/env python3
from pathlib import Path
import re

root = Path.cwd()
css = root / "assets/css/main.css"
partial = root / "layouts/partials/page-teams.html"

# Move any accidental backup files out of Hugo data processing paths
backup_dir = root / ".backups" / "teamcentral-black-header-toggle"
backup_dir.mkdir(parents=True, exist_ok=True)
for p in list((root / "data").glob("*.bak*")) if (root / "data").exists() else []:
    p.rename(backup_dir / p.name)

# Template-level cleanup where possible. Keep this conservative so it works across prior iterations.
if partial.exists():
    text = partial.read_text()
    bak = backup_dir / "page-teams.html.bak"
    if not bak.exists():
        bak.write_text(text)

    # Remove standalone selector/helper intro blocks if they exist from older patches.
    # These phrases will be reintroduced in the dark season header via CSS/HTML below.
    text = text.replace("Choose a season to view active and upcoming Rawlings Tigers NOVA teams.", "")
    text = text.replace("Rawlings Tigers NOVA seasons run fall through spring.", "")
    text = text.replace("Spring and fall teams are grouped together under one baseball season.", "")

    # Remove common small Select Season label blocks if present.
    text = re.sub(r'(?s)<p class="[^"]*(?:rt-kicker|kicker|team-central[^" ]*kicker)[^"]*">\s*Season\s*</p>\s*', '', text)
    text = re.sub(r'(?s)<h2[^>]*>\s*Select Season\s*</h2>\s*', '', text, flags=re.I)
    text = re.sub(r'(?s)<h3[^>]*>\s*Select Season\s*</h3>\s*', '', text, flags=re.I)

    # Add helper text inside season title blocks when we can find a season range line.
    # Avoid duplicating if already present.
    if "Choose a season to view active and upcoming" not in text:
        # First try to add after the season range line in a broad way.
        text = re.sub(
            r'(<[^>]+class="[^"]*(?:season[^" ]*(?:range|meta)|team-season[^" ]*(?:range|meta))[^"]*"[^>]*>.*?</[^>]+>)',
            r'\1\n<p class="team-season-dashboard__help">Choose a season to view active and upcoming Rawlings Tigers NOVA teams. Seasons run fall through spring.</p>',
            text,
            count=1,
            flags=re.S,
        )

    partial.write_text(text)

# CSS overrides: remove white selector panel visual, move/treat toggle as part of dark header via layout,
# make black section rounded top, and add helper text styling. These are broad selectors to match the prior generated classes.
css.parent.mkdir(parents=True, exist_ok=True)
marker = "/* Team Central black season header toggle cleanup */"
existing = css.read_text() if css.exists() else ""
block = r'''

/* Team Central black season header toggle cleanup */
/* Remove the separate white Select Season card treatment so the black season panel becomes the main dashboard header. */
.rt-team-season-selector,
.team-season-selector,
.team-central-season-selector,
.rt-season-selector,
.season-selector-card,
.team-central__selector,
.team-dashboard__selector,
.team-season-dashboard__selector {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* Hide redundant standalone Select Season headings/labels when older markup is still present. */
.rt-team-season-selector h2,
.rt-team-season-selector h3,
.team-season-selector h2,
.team-season-selector h3,
.team-central-season-selector h2,
.team-central-season-selector h3,
.rt-season-selector h2,
.rt-season-selector h3,
.season-selector-card h2,
.season-selector-card h3,
.team-central__selector h2,
.team-central__selector h3,
.team-dashboard__selector h2,
.team-dashboard__selector h3,
.team-season-dashboard__selector h2,
.team-season-dashboard__selector h3,
.rt-team-season-selector .rt-kicker,
.team-season-selector .rt-kicker,
.team-central-season-selector .rt-kicker,
.rt-season-selector .rt-kicker,
.season-selector-card .rt-kicker,
.team-central__selector .rt-kicker,
.team-dashboard__selector .rt-kicker,
.team-season-dashboard__selector .rt-kicker {
  display: none !important;
}

/* Make the selected season panel the rounded top of the dashboard. */
.rt-team-season-summary,
.team-season-summary,
.team-central-season-summary,
.rt-team-season-hero,
.team-season-hero,
.team-season-dashboard__summary,
.team-dashboard__season-header,
.team-season-dashboard__header {
  position: relative !important;
  overflow: hidden !important;
  border-radius: 18px 18px 0 0 !important;
  margin-top: 0 !important;
  margin-bottom: 0 !important;
  border-bottom: 4px solid var(--brand, #f15a24) !important;
  padding: clamp(2rem, 4vw, 3.25rem) clamp(1.5rem, 4vw, 3rem) !important;
}

/* If the toggle still lives in the selector markup, visually pull it into the black season header area. */
.rt-team-season-toggle,
.team-season-toggle,
.team-central-season-toggle,
.season-toggle,
.team-season-dashboard__toggle,
.team-dashboard__toggle {
  position: relative !important;
  z-index: 3 !important;
  margin-left: auto !important;
  margin-bottom: -4.25rem !important;
  transform: translateY(1.1rem) !important;
  width: max-content !important;
  max-width: 100% !important;
}

/* Keep the toggle readable on the black header. */
.rt-team-season-toggle a,
.rt-team-season-toggle button,
.team-season-toggle a,
.team-season-toggle button,
.team-central-season-toggle a,
.team-central-season-toggle button,
.season-toggle a,
.season-toggle button,
.team-season-dashboard__toggle a,
.team-season-dashboard__toggle button,
.team-dashboard__toggle a,
.team-dashboard__toggle button {
  text-decoration: none !important;
}

/* Helper copy belongs inside the black season header, not in a separate white Select Season block. */
.team-season-dashboard__help,
.team-dashboard__help,
.team-season-summary__help {
  max-width: 48rem;
  margin: .9rem 0 0;
  color: rgba(255,255,255,.72);
  font-weight: 700;
  line-height: 1.55;
  letter-spacing: .01em;
}

/* Remove extra whitespace left by the old selector block. */
.rt-team-central__body,
.team-central__body,
.team-season-dashboard,
.rt-team-season-dashboard {
  padding-top: clamp(1rem, 2vw, 1.5rem) !important;
}

/* Tighten the first term under the black header so the dashboard feels connected. */
.rt-team-season-summary + .rt-team-term,
.team-season-summary + .team-term,
.team-central-season-summary + .team-central-term,
.rt-team-season-hero + .rt-team-term,
.team-season-hero + .team-term,
.team-season-dashboard__summary + .team-term,
.team-dashboard__season-header + .team-term,
.team-season-dashboard__header + .team-term {
  margin-top: clamp(1.5rem, 3vw, 2.25rem) !important;
}

@media (max-width: 760px) {
  .rt-team-season-toggle,
  .team-season-toggle,
  .team-central-season-toggle,
  .season-toggle,
  .team-season-dashboard__toggle,
  .team-dashboard__toggle {
    width: 100% !important;
    margin: 0 0 1rem 0 !important;
    transform: none !important;
  }

  .rt-team-season-summary,
  .team-season-summary,
  .team-central-season-summary,
  .rt-team-season-hero,
  .team-season-hero,
  .team-season-dashboard__summary,
  .team-dashboard__season-header,
  .team-season-dashboard__header {
    border-radius: 16px 16px 0 0 !important;
    padding: 1.4rem !important;
  }

  .team-season-dashboard__help,
  .team-dashboard__help,
  .team-season-summary__help {
    font-size: .92rem;
  }
}
'''
if marker not in existing:
    css.write_text(existing.rstrip() + block + "\n")
else:
    # replace existing block from marker to EOF-ish if it was the last thing; safer append v2 marker
    css.write_text(existing.rstrip() + block.replace(marker, marker + " v2") + "\n")

print("Applied Team Central black header toggle cleanup.")
print("Moved data backups to:", backup_dir)
