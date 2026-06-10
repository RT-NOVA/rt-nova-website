# Patch Notes v13 — Org Logo and Baseball Icons

## What changed

- Replaced the temporary NOVA/RT text marks in the global header and footer with a local copy of the Rawlings Tigers Northern Virginia round logo.
- Added the logo asset locally at:
  - `static/images/teamlinkt/rawlings-tigers-nova-round-logo.png`
- Updated the global header partial:
  - `layouts/partials/site-header.html`
- Updated the global footer partial:
  - `layouts/partials/site-footer.html`
- Reworked the homepage icon set to use more baseball/program-specific line icons:
  - baseball
  - diamond
  - clipboard
  - home plate
  - batting helmet
  - jersey
  - family
  - shield
- Updated homepage data icon references in:
  - `data/homepage.yaml`
- Updated the icon partial:
  - `layouts/partials/icon.html`
- Added CSS overrides in:
  - `assets/css/main.css`

## Validation

Run:

```bash
rm -rf public resources .hugo_build.lock
./scripts/validate-local-assets.sh
hugo server -D
```

Also confirm there are no external TeamLinkt CDN references:

```bash
grep -R "cdn-app\.teamlinkt\.com" -n . --exclude-dir=.git
```
