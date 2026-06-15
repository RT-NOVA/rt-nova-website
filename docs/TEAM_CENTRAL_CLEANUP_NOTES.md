# Team Central Cleanup Notes

This update focuses on the `/teams/` page visual cleanup:

- Removes the decorative right-side NOVA/Rawlings Tigers card from the Team Central hero.
- Moves the season explanation under the season selector intro.
- Lightens Spring/Fall season sections so the page feels less like nested white boxes.
- Replaces heavy archived team listings with a compact archive callout when the template pattern can be matched.
- Adds responsive guardrails for the archive callout.

Run from repo root:

```bash
python3 scripts/apply-team-central-cleanup.py
hugo server -D
```

The script backs up `layouts/partials/page-teams.html` before changing it:

```text
layouts/partials/page-teams.html.bak-teamcentral-cleanup
```
