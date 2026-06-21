# Accolades Overlay Banner Template Patch

## What changed

- Updates the Banner Wall to use a realistic blank banner image template.
- Overlays tournament logo, season/year, and result from YAML.
- Moves tournament/year/team text into a clean caption below the banner.
- Adds the uploaded 13U Black tournament logo assets.
- Keeps Previous / Next pager and centers the last page when only 1 or 2 banners remain.
- Leaves Current Team Results and Player Honors in their existing structure.

## New YAML pattern

```yaml
banner_wall:
  - order: 1
    year: "2026"
    season: "Spring"
    tournament: "March Mania"
    team: "13U Black"
    result: "Runner-Up"
    logo: "/images/accolades/tournament-logos/march-mania-logo.png"
    template: "/images/accolades/blank-white-hanging-banner.svg"
```

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-accolades-overlay-banner-template-patch.zip -d .

hugo server -D --disableFastRender --ignoreCache
```

Then hard refresh:

```text
Cmd + Shift + R
```

## Verify

```bash
rg -n 'blank-white-hanging-banner|accolades-overlay-banner|tournament-logos|banner_wall' data/accolades.yaml layouts/partials/page-accolades.html assets/css/accolades.css
ls -l static/images/accolades/tournament-logos/
```
