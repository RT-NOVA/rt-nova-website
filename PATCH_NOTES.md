# Sponsorship Opportunities Refresh Patch

This patch renames the sponsorship page from `/sponsors/` to `/sponsorship-opportunities/` and refreshes the content using the old TeamLinkt sponsorship page as the content source while preserving the new Hugo site look and feel.

## Apply

```bash
unzip -o ~/Desktop/rt-nova-sponsorship-opportunities-refresh-patch.zip -d .
python3 scripts/apply-sponsorship-opportunities-refresh.py
hugo server -D --disableFastRender
```

## Updated references

Current sponsorship CTAs and nav links now point to `/sponsorship-opportunities/`. The `/sponsors/` path is intentionally left available for a future sponsor showcase page.
