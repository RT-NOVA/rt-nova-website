# Patch Notes — Team Central Archive Grouping Fix

## Summary
- Keeps the Team Central Archive search UI and display formatting intact.
- Updates Archive result ordering so the same team/season entries stay together instead of all Fall teams appearing before all Spring teams.

## Details
- Archive rows now carry explicit sort metadata for team sort order and term order.
- Archive rows are sorted client-side by:
  1. Season year, newest first
  2. Team sort order from `data/seasons/<year>/teams.yaml`
  3. Team name
  4. Term order, Fall then Spring
- This keeps entries like `13U Black — Fall 2025` and `13U Black — Spring 2026` adjacent in the 2026 archive view.

## Files Changed
- `layouts/partials/page-teams.html`
- `PATCH_NOTES.md`

## Team Central Archive fall-before-spring grouping patch

- Updated Team Central Archive sorting so Fall rows stay before Spring rows within each team group.
- Archive rows are ordered by season, team group order, team name, then term order.
- This keeps same-team Fall/Spring rows together even if the term data has different sort order values.

---

## Team Central Archive numeric season dropdown patch

- Updated the Team Central Archive Season dropdown to keep seasons in numeric descending order.
- The current season remains in its year-based position and is labeled `Current Season · <Year> Season`.
- Example ordering: `2027 Season`, `Current Season · 2026 Season`, `2025 Season`.
- If `2028 Season` is added while `2027 Season` is current, the dropdown will order as `2028 Season`, `Current Season · 2027 Season`, `2026 Season`.

## Homepage Photo Integration Patch

- Added data-driven hero image focus control through `data/homepage.yaml`.
- Added an optional image element inside the existing “Built around growth, competition, and love for the game” section.
- Kept the homepage structure intact; no new standalone photo-story/gallery section was added.
- Added `docs/HOMEPAGE_MEDIA.md` with hero and section image update instructions.

## Homepage local training teaser with photos preserved

- Preserved the data-driven homepage hero image and Built Around Growth photo support.
- Added a compact local/training teaser inside the existing Built Around Growth section.
- Added callouts for Local roots and Real training locations with a link to `/training-locations/`.
- Updated homepage proof points to emphasize Woodbridge-based roots, outdoor + indoor training, age groups, and the Rawlings Tigers brand.
- Updated `docs/HOMEPAGE_MEDIA.md` with photo and teaser configuration notes.
