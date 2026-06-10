# v15 - Iconify / Game Icons replacement

- Replaced the homepage Bootstrap-style program icons with locally bundled Game-icons.net SVG icons.
- Added a local icon folder at `assets/icons/game-icons/`.
- Updated `layouts/partials/icon.html` to prefer Game Icons and fall back to existing local social/bootstrap icons.
- Updated `data/homepage.yaml` so the homepage program cards use baseball/program-specific icon names.
- Added `/credits/` page for Game-icons.net attribution.
- Added `assets/icons/game-icons/ATTRIBUTION.md` for maintainers.
- Added `Icon Credits` link to the global footer.

The icons are locally hosted and do not require Iconify, Game-icons.net, or any external CDN at runtime.
