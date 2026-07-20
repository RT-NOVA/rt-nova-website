# Header and navigation

Normal navigation labels, ordering, and destinations are driven by:

```text
data/navigation.yaml
```

## Files

- `data/navigation.yaml` — primary and utility navigation data.
- `layouts/partials/site-header.html` — global header structure and shortcuts.
- `layouts/partials/site-nav-item.html` — link and dropdown rendering.
- `assets/css/header-nav.css` — header, dropdown, and mobile-menu styling.
- `assets/js/header-nav.js` — disclosure controls, mobile menu, and scroll state.

## Current behavior

- The desktop logo is centered with supporting information/actions on either side.
- Hero pages start with a transparent header and transition to solid black after scrolling.
- Pages without a compatible hero use the solid header immediately.
- Dropdowns work with hover/focus on desktop and click/tap disclosure controls.
- Escape and outside click close open menus.
- Mobile uses a compact header and a scrollable menu.
- Watch Now is available in the Teams dropdown and through the camera shortcut.

Transparent-header spacing belongs to the real hero components, such as `.rt-page-hero` and `.rt-page-hero__inner`. Do not apply spacing to arbitrary first children of `main`.

## Navigation structure

Top-level items are listed under `main`. Items render in the exact YAML order:

```yaml
main:
  - name: Home
    url: /
  - name: Teams
    children:
      - name: Team Central
        url: /teams/
      - name: Watch Now
        url: /watch-now/
  - name: Tryouts
    url: /tryouts/
```

A top-level item with `children` becomes a dropdown. A normal link needs only `name` and `url`. Utility actions such as Join Our Staff live under `utility`.

Use site-root paths for internal links and full HTTPS URLs for outside destinations.

## Adding a link

1. Add the item to the appropriate list in `data/navigation.yaml`.
2. Keep child indentation beneath its parent.
3. Confirm the destination exists.
4. Test desktop keyboard/mouse behavior and the mobile disclosure menu.
5. Check that the navigation still fits at medium desktop widths.

Do not add `weight`; YAML ordering controls the display order.

## Header shortcuts

Icon-only actions must include an accessible label or title. The camera shortcut should continue to link to `/watch-now/`; Facebook and Instagram should use the official program URLs.

Shortcuts are part of the header template, not the main YAML navigation list, so changes to them require checking `layouts/partials/site-header.html` as well as the desktop and mobile layouts.

## Dropdown styling

The header uses one white hover/open underline system. Avoid adding a second effect with `border-bottom`, `text-decoration`, or an additional pseudo-element.

At the transparent top state, dropdowns use the established overlay treatment. In the scrolled state, they sit naturally against the solid black header. Update the existing rules in `assets/css/header-nav.css` rather than appending a global override.

## Troubleshooting

### A dropdown is always open

Check that `children` is nested beneath the intended parent and that the page is loading `assets/js/header-nav.js`.

### A menu is clipped or cannot scroll on mobile

Inspect the mobile menu's height and overflow rules in `assets/css/header-nav.css`. Do not lock the entire page merely to show the menu; users must be able to reach every navigation item.

### Transparent header overlaps a page title

Compare the affected hero with a known-good `.rt-page-hero`. Safe-area spacing should be applied once to `.rt-page-hero__inner`, not once on the outer hero and again on the inner wrapper.

### A header change does not appear

Run Hugo with fast render disabled and hard-refresh the browser:

```bash
hugo server -D --disableFastRender
```

## Validation

Check at least:

```text
1440px wide desktop
1100–1300px medium desktop
768–1024px tablet
390–430px mobile
```

Verify the transparent top state, black scrolled state, desktop dropdowns, mobile menu scrolling, keyboard focus, and the Watch Now/social shortcuts. Then run the production validation from [`FRONTEND_MAINTENANCE.md`](FRONTEND_MAINTENANCE.md).
