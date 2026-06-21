# Coaches Season Staff

Adds season-aware tabs to the Team Coaching Staff section on `/coaches/`.

## Behavior

- The current season is shown by default.
- Current and upcoming seasons are separated into their own tabs.
- The page uses the split season data from `data/seasons/index.yaml` and `data/seasons/<season-id>/teams.yaml`.
- Staff rows are team-first, not coach-first.
- Each season uses the latest populated term in the season file:
  - Spring teams if present.
  - Otherwise Fall teams.
- Assistant coach details and head coach bios are still pulled from `data/coaches.yaml` when the team name matches.
- Older teams sort first because rows use `sort_order` from the season team data.

## Why

This avoids mixing current and upcoming teams in one long list and prevents duplicated-looking rows such as the same coach appearing for both a current team and an upcoming team.

## v2 visual cleanup

- Removed the visible season date/cycle line from the Coaches page season heading.
- Kept season cycle data in `data/seasons/index.yaml` because other pages, such as Team Central, still use it.
- Changed the active Coaches season tab to a solid orange selected state instead of an orange underline.
