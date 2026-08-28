# Managing Sponsors

Sponsor content is managed in `data/sponsors.yaml`. Approved logo files are stored in `static/images/sponsors/`.

## Data structure

The file contains three sections:

- `intro`: introductory copy displayed near the top of the Sponsors page.
- `levels`: the sponsorship hierarchy and the order in which levels appear.
- `current`: the active sponsors displayed on the Sponsors page.

Only levels containing at least one active sponsor are shown publicly.

## Sponsor fields

Each entry under `current` supports these fields:

| Field | Required | Purpose |
| --- | --- | --- |
| `name` | Yes | Sponsor name used for accessibility and optional visible text. |
| `level` | Yes | Must exactly match a `name` under `levels`. |
| `website` | Yes | Destination opened when a visitor selects the logo or visible name. |
| `image` | Yes | Logo used on the light Sponsors page. Use a root-relative `/images/sponsors/...` path. |
| `homepage_image` | No | Alternate logo for the dark homepage sponsor band. When omitted, `image` is used. |
| `image_alt` | Yes | Concise description of the logo for visitors using assistive technology. |
| `show_name` | No | Set to `false` when the logo already includes the sponsor name. Defaults to showing the name. |
| `tagline` | No | One short sentence displayed beneath the logo. |

Example:

```yaml
current:
  - name: Sponsor Name
    level: Single
    website: https://www.example.com/
    image: /images/sponsors/sponsor-name-dark.png
    homepage_image: /images/sponsors/sponsor-name-light.png
    image_alt: Sponsor Name
    show_name: false
    tagline: A short description of the sponsor's community support.
```

## Adding a sponsor

1. Add approved logo files to `static/images/sponsors/`. Use transparent backgrounds when possible and provide versions suitable for both light and dark backgrounds.
2. Add a new entry under `current` in `data/sponsors.yaml`.
3. Assign a `level` that exactly matches one of the configured level names.
4. Keep the tagline brief and omit dates, donation amounts, and long descriptions.
5. Build and validate the site before publishing.

Every entry under `current` appears in the homepage sponsor rail. The list order controls the left-to-right logo order; keep higher sponsorship levels first and group sponsors at the same level together.

## Managing sponsorship levels

The order of entries under `levels` controls the hierarchy displayed on the page. Each level has:

- `name`: the public level name and the exact value sponsors must use in their `level` field.
- `slug`: the lowercase, hyphenated identifier used by the page layout.

Reorder existing level entries to change their display order. Renaming or adding a level also requires reviewing the Sponsorship Opportunities content and the sponsor-card layout styles so the public hierarchy stays consistent.

## Changing a sponsorship level

Update the sponsor's `level` value. The Sponsors page automatically moves the card into the matching section and hides any level that becomes empty.

Do not add dollar amounts to `data/sponsors.yaml`; sponsorship pricing belongs on the Sponsorship Opportunities page.

## Removing a sponsor

Remove the sponsor's complete entry from `current` when the sponsorship ends. Logo files may remain in `static/images/sponsors/` if they are still used by a news article; otherwise they can be removed separately.

## Display behavior

Sponsor cards use a level badge, clickable logo, optional visible name, and short tagline. Incomplete rows are centered automatically. The page intentionally omits sponsorship dates, level descriptions, and separate visit links.

## Validation

From the site repository, run:

```bash
hugo --minify --cleanDestinationDir
bash scripts/validate-local-assets.sh
bash scripts/validate-site.sh public
```
