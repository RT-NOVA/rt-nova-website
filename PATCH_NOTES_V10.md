# v10 Header Refinement

This update refines the global Hugo header to more closely follow the Twelve Baseball-style screenshot:

- Replaced the two-tier header with a single dark premium navigation bar.
- Added a larger left-aligned Rawlings Tigers NOVA text mark.
- Moved navigation, social shortcuts, and the signup CTA into one row.
- Added responsive mobile behavior that keeps the same global header template across all pages.
- Header remains defined once in `layouts/partials/site-header.html` and rendered globally from `layouts/_default/baseof.html`.

No page-level header duplication was added.
