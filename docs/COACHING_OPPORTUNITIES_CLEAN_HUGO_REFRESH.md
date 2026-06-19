# Coaching Opportunities Clean Hugo Refresh

This patch reworks `/coaching-opportunities/` using the latest uploaded site ZIP as the base.

## Design direction

The page is moved away from the older-site feel and closer to the newer Hugo pages:

- smaller centered kicker / heading / note blocks
- clean role cards
- compact comparison rows instead of large black-header tables
- no split-feature giant headline sections
- no orange side bars on cards
- light support cards instead of the heavy dark support band
- a simpler application panel

## Files

- `layouts/partials/page-coaching-opportunities.html`
- `assets/css/coaching-opportunities.css`

## Content source

Most wording still comes from `data/coaching_opportunities.yaml`.
