# Front-end maintenance guide

The rendered site is the design baseline. Front-end changes should be made in the file that owns the component, then checked at the responsive widths listed in the root README.

## Asset loading

`layouts/partials/head/styles.html` is the single source of truth for global and route-level stylesheet loading. It builds one fingerprinted core bundle in this order:

1. `foundation.css` — tokens, reset, typography, containers, buttons, and grids.
2. `shared-components.css` — shared sections, cards, page heroes, and data-driven components.
3. `team-central-*.css` — the established Team Central cascade, split into bounded modules.
4. `page-components.css` — Family Hub, Booster Club, sponsorship, and roster support styles.
5. `tryouts-foundation.css` — the original Tryouts component foundation.
6. `theme-system.css` — final brand colors and heading tiers.
7. `homepage.css` — homepage-only component presentation.

Do not reorder these modules casually. They preserve the previous `main.css` cascade exactly; the only declaration-level cleanup made during the split was removal of one repeated, byte-identical Team Central block.

Global component styles follow the core bundle. Page-only styles are selected in `layouts/partials/body/page-styles.html`. They remain immediately before page content because the preserved hero behavior distinguishes pages that have an asset node before the hero. This compatibility detail is documented in that partial and should be removed only as part of a separately validated hero-cascade migration.

## CSS ownership

| Component | Primary stylesheet |
|---|---|
| Header and navigation | `assets/css/header-nav.css` |
| Transparent subpage heroes | `assets/css/page-hero.css` |
| Locked visual baseline | `assets/css/design-lock.css` |
| Homepage | `assets/css/homepage.css` |
| Social Hub | `assets/css/social-hub.css`, `assets/css/social-hub-home.css` |
| Team Central | `assets/css/team-central-*.css` |
| Footer | `assets/css/footer-cleanup.css`, `assets/css/footer-brick.css` |
| Page-specific layouts | the matching file in `assets/css/` |

`design-lock.css` is intentionally a compact preservation layer captured from the approved design. Avoid editing it for routine component work. Prefer the component stylesheet that owns the element.

When changing CSS:

- Edit the existing owning rule instead of adding a new override at the end of another file.
- Keep selectors scoped to the component.
- Avoid generic `main > :first-child` or `section:first-child` fixes.
- Do not add `!important` unless the owning component already requires it to preserve the approved cascade.
- Run `git diff --check`, the Hugo production build, and responsive browser checks before committing.

## Typography and heading hierarchy

Typography should follow a small number of roles instead of being tuned independently on each page:

- **Major page and section headings:** the established heavy uppercase display treatment.
- **Compact content-block headings:** smaller display headings for cards, feature copy, and supporting sections.
- **Data and list headings:** readable sans-serif headings for tables, filters, schedules, rosters, and dense information.
- **Eyebrows and navigation:** small uppercase text with deliberate letter spacing.
- **Body copy:** the shared readable sans-serif family and line height.

Heading hierarchy and layout alignment are separate decisions. A centered section does not need a larger heading, and a left-aligned data section should not invent a new type family. Check `assets/css/theme-system.css` and the owning component stylesheet before adding a new font size or weight.

## JavaScript ownership

`layouts/partials/head/scripts.html` is the single script registry. Scripts are deferred, fingerprinted, and loaded only on pages that use them.

| Behavior | Script |
|---|---|
| Header, mobile menu, scroll state | `assets/js/header-nav.js` |
| Homepage and archive Social Hub paging | `assets/js/social-hub.js` |
| Team season/archive controls | `assets/js/teams.js` |
| Coach season controls and photo modal | `assets/js/coaches.js` |
| Tryout filtering | `assets/js/tryouts.js` |
| Accolade filters and paging | `assets/js/accolades.js` |
| Schedule filtering and expansion | `assets/js/schedules.js` |

Page scripts should query from a page-specific root element when possible and exit immediately when that root is absent.

## Required validation

Run:

```bash
hugo --minify --cleanDestinationDir
bash scripts/validate-local-assets.sh
bash scripts/validate-site.sh public
```

Then inspect the homepage and representative inner pages at phone, tablet, and desktop widths. Verify the mobile menu, transparent-to-solid header transition, Team Central season controls, Social Hub pager, and any page control affected by the change.
