# Coaches Page

The `/coaches/` page is a compact program-wide staff directory.

## Design intent

This page is closer to Family Hub, Team Central, and roster pages than the Coaching Opportunities page.

- Post-hero section headings are smaller and left-aligned.
- Program leadership stays compact.
- Team staff is one row per team on desktop.
- Head coaches have expandable bios.
- Coaching standards are secondary support cards.

## Files

- `data/coaches.yaml`
- `layouts/partials/page-coaches.html`
- `assets/css/coaches.css`

## Editing coaches

Update `data/coaches.yaml`.

Team staff rows are listed under `team_staff`.
Head coach bios live under each team staff entry as `head_coach.bio`.

## Styling

Keep future styling scoped to `assets/css/coaches.css`.
Avoid global overrides in `assets/css/main.css` unless the entire design system is intentionally changing.
