# Program Media Asset Cleanup

This patch moves locally stored program media into a neutral asset folder and updates source references to the new path.

## What changed

- Local program media now lives under `static/images/program-media/`.
- Source references now use `/images/program-media/...`.
- Header and footer logo paths now use `/images/program-media/rawlings-tigers-nova-round-logo.png`.
- Data files, markdown content, and docs use neutral program media naming.

## Cleanup note

After applying this patch, remove the previous legacy media folder and generated output from your working tree before rebuilding the site.
