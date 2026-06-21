# Teams Accolades Link Cleanup

Removes Accolades/Tournament Results links from the `/teams/` page data and cleans up unused Teams table rendering logic.

## Files

- `data/teams.yaml`
- `layouts/partials/team-table-term.html`
- `assets/css/team-central.css`

## Changes

- Removed `12` `Accolades` placeholder link entries from `data/teams.yaml`.
- Removed Accolades-specific icon/class handling from `team-table-term.html`.
- Removed unused Accolades-specific Teams CSS and updated placeholder comments to be generic.
- Preserved current team data from the prior Accolades work, including the 10U current team entry.
