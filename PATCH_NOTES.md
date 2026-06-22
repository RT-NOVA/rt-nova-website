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

## Training Locations outdoor grid

- Renamed `Woodbridge Outdoor Field Locations` to `Outdoor Field Locations`.
- Updated outdoor location cards so 3 cards fit in one desktop row and 4 cards form a 2x2 desktop grid.

## Accolades season label display tweak

- Added the season label directly under each Tournament Results team name so repeated/archive team names are easier to distinguish while preserving the existing visual layout.

## Accolades team season label follow-up

- Kept the Tournament Results display styling intact.
- Made the season label a dedicated stacked line directly under each Tournament Results team name.
- Added targeted CSS so the season line remains visible below the team heading instead of being visually swallowed by the heading/count row.

## Accolades Player Honors Carousel Spacing Patch

- Added spacing between Player Honors images, player text, and Previous / Next carousel controls.
- Kept the open cream-background Player Honors treatment intact.
- No data, filter, or Tournament Results logic changed.

## Accolades tournament results open layout tweak

- Removed tournament logo rendering from Tournament Results cards.
- Kept Tournament Results grouped by team/season, but made each result item text-only.
- Reinforced the open, less-boxed Tournament Results treatment so it feels closer to the Player Honors section.

## Accolades Tournament Logos Restore

- Restored tournament logo rendering inside Tournament Results cards.
- Kept the newer open Tournament Results layout and Player Honors carousel behavior unchanged.

## Accolades Tournament Logo Visibility Fix

- Restored visible tournament logos in the open Tournament Results layout.
- Kept the outer team groups open/airy without the larger card treatment.
- No Player Honors or filter/search logic changes.

## Accolades Tournament Results Partial Row Centering

- Updated Tournament Results carousel rows to center partial pages, matching Player Honors behavior.
- A single visible tournament card is centered.
- Two visible tournament cards are centered as a pair.
- Three visible tournament cards continue to display as a normal row.
- Kept the current open Tournament Results layout, tournament logos, and filter/search logic unchanged.
