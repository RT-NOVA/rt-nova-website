# Team Central Season Dashboard Update

This update changes `/teams/` from separate stacked season/term blocks into one unified season dashboard card.

## Files changed

- `layouts/partials/page-teams.html`
- `layouts/partials/team-table-term.html`
- `scripts/apply-team-central-season-dashboard.py`

## Apply

```bash
unzip -o rt-nova-team-central-season-dashboard-update.zip -d .
python3 scripts/apply-team-central-season-dashboard.py
hugo server -D
```

## Layout intent

The selected season now appears as one cohesive dashboard:

- Season selector header
- Selected season summary
- Spring subsection
- Fall subsection

On mobile, the table rows convert into stacked mini-panels so the page avoids horizontal scrolling.
