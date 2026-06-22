# Family Hub Page

The `/family-hub/` page is rendered by:

```text
content/family-hub.md
layouts/partials/page-family-hub.html
```

The markdown file only controls the page title, description, and template selection. The page layout and cards live in the partial so the Family Hub can match the rest of the custom Hugo site design.

## Updating family resource links

Edit:

```text
layouts/partials/page-family-hub.html
```

Common updates include:

- changing the Dick’s Sporting Goods coupon URL
- updating apparel store links
- adding or removing gear store cards
- changing Booster Club, Sponsorship, or Social Hub CTAs

## Design notes

The page intentionally uses the new RT NOVA Hugo design system. Content was adapted from the old legacy site Family Hub page, but the old expand/collapse layout was not copied.
