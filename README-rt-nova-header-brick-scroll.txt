RT NOVA Brick-style scroll header preview

Files changed:
- layouts/partials/site-header.html
- assets/css/header-nav.css
- assets/js/header-nav.js
> Historical note: the one-time migration script referenced here was removed after its changes were applied. The current source and Git history are authoritative.

Behavior:
- Header is fixed over hero sections.
- At the top of hero pages, the header is translucent/opaque over the image.
- After scrolling a small amount, the header transitions to solid black.
- For pages without a detected hero as the first main section, the header stays black and the page is padded down.
- Mobile remains a compact black header with the existing menu behavior.

Hero detection selectors in assets/js/header-nav.js:
.home-hero, .page-hero, .rt-page-hero, .team-hero, .hero, [data-hero]

To undo from repo root:
