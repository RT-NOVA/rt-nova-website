# About Page Refresh Patch

This patch updates `/about/` to use content adapted from the old TeamLinkt About page while keeping the current Rawlings Tigers NOVA Hugo site layout/classes.

Files included:

- `content/about.md`
- `layouts/partials/page-about.html`
- `scripts/apply-about-page-refresh.py`

Run the script after extraction so `layouts/_default/single.html` is updated safely without overwriting unrelated template changes.
