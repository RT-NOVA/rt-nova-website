# Patch Notes v14 — Local Bootstrap-Style Icon Cleanup

- Replaced the earlier custom inline icon switch with local SVG files under `assets/icons/bootstrap/`.
- Updated the Hugo `icon.html` partial to render local SVG files by name.
- Updated homepage pillar/card icon assignments to use a cleaner, more consistent professional icon set.
- Kept social icons local and rendered through the same Hugo icon partial.
- Added aliases so older icon names still resolve cleanly:
  - `x` → `twitter-x`
  - `clipboard` → `clipboard-check`
  - `family` → `house-heart`
  - `shield` → `shield-check`

Note: this environment could not reach the public Bootstrap Icons CDN, so the icons are bundled locally as SVG assets using Bootstrap Icons-style naming and a consistent SVG approach. No external icon CDN is required for Cloudflare Pages.
