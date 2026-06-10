# Patch Notes v16 - GitHub Pages project-path image fix

This patch fixes image and internal link paths when the site is deployed as a GitHub Pages project site, for example:

`https://smbambling.github.io/rt-nova-website/`

## What changed

- Added `layouts/partials/url.html`.
- Updated templates to pass local image paths and internal links through `relURL`.
- Header/footer logo paths now include the GitHub Pages project base path during Hugo builds.
- Team, coach, tryout, accolade, and homepage image paths now render correctly under project-path deployments.
- External links, anchors, `mailto:`, and `tel:` links are left unchanged.

## Why

Root-relative URLs like `/images/teamlinkt/logo.png` work on a root domain, but fail on GitHub Pages project sites because the site lives under `/rt-nova-website/`.

The correct rendered URL should be:

`/rt-nova-website/images/teamlinkt/logo.png`

when built with:

`hugo --baseURL "https://smbambling.github.io/rt-nova-website/"`
