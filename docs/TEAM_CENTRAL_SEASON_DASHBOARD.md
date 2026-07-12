# Team Central Season Dashboard Update

This update changes `/teams/` from separate stacked season/term blocks into one unified season dashboard card.

## Files changed

- `layouts/partials/page-teams.html`
- `layouts/partials/team-table-term.html`
> Historical note: the one-time migration script referenced here was removed after its changes were applied. The current source and Git history are authoritative.

## Apply

```bash
unzip -o rt-nova-team-central-season-dashboard-update.zip -d .
hugo server -D
```

## Layout intent

The selected season now appears as one cohesive dashboard:

- Season selector header
- Selected season summary
- Spring subsection
- Fall subsection

On mobile, the table rows convert into stacked mini-panels so the page avoids horizontal scrolling.
