# v11 Footer Patch

This version updates the global footer to follow the Twelve Baseball-inspired layout more closely while keeping the Rawlings Tigers NOVA theme.

## Changed

- Rebuilt `layouts/partials/site-footer.html` as a single global footer partial.
- Added a large left-side NOVA/RT brand mark similar to the Twelve footer composition.
- Reorganized footer links into `Quick Links`, `Resources`, `Support`, and `Follow` sections.
- Updated `data/footer.yaml` so footer navigation can be maintained without editing HTML.
- Added v11 footer CSS overrides in `assets/css/main.css`.

## Validation

Run:

```bash
rm -rf public resources .hugo_build.lock
./scripts/validate-local-assets.sh
grep -R "cdn-app\.teamlinkt\.com" -n . --exclude-dir=.git --exclude-dir=public
hugo server -D
```
