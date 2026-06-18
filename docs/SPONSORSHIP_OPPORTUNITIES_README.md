# Sponsorship Opportunities Page

The sponsorship opportunities page lives at:

```text
/sponsorship-opportunities/
```

The old `/sponsors/` URL has been intentionally freed up so a future page can showcase current sponsors.

## Main files

```text
content/sponsorship-opportunities.md
layouts/partials/page-sponsorship-opportunities.html
data/sponsorship_opportunities.yaml
```

## Updating sponsorship content

Most editable sponsorship content is in:

```text
data/sponsorship_opportunities.yaml
```

You can update package names, amounts, features, impact items, contact information, and benefit comparison rows there.

## Sponsorship package examples

```yaml
packages:
  - name: Single
    amount: "$250"
    features:
      - Sponsor plaque / framed team picture
      - Social media recognition, 1 post
```

## Benefit comparison

The benefits table is generated from the `benefits:` list in the data file. Keep values short so the table remains readable on desktop and scrollable on mobile.
