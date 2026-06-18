# Social Hub Page Fix Patch

This patch fixes the broken Social Hub page/tab update by:

- creating `layouts/social-hub/list.html`
- making `content/social-hub/_index.md` render the `/social-hub/` section page
- fixing homepage pager selectors so only 3 cards show at a time
- adding reusable `layouts/partials/social-hub-card.html`
- keeping `/social-hub/` sorted newest-to-oldest with tabs for All, Team News, Facebook, and Instagram
- adding a cleanup script for misplaced folders from the previous patch

After unzipping, run:

```bash
python3 scripts/apply-social-hub-page-fix.py
hugo server -D --disableFastRender
```
