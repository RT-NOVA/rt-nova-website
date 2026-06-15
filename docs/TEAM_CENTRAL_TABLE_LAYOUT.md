# Team Central themed table layout

This update changes `/teams/` from card-heavy team profiles to a themed table/list layout.

## Files

- `layouts/partials/page-teams.html`
- `layouts/partials/team-table-term.html`
- `scripts/apply-team-central-table-layout.py`

Run the script after unzipping to append the required CSS to `assets/css/main.css`.

## Behavior

- Season selector remains at the top.
- Selected season renders Spring/Fall groups.
- Each group uses a compact, themed team table.
- On mobile, each table row turns into a stacked mini-panel.
- Past seasons remain compact behind a collapsed archive section.
