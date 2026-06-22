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
