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

The seasonal team list and head-coach assignment originate in `data/seasons/<season-id>/teams.yaml`. A team with `enabled: false` is omitted from that season's coaching table, while its reusable bio may remain in `data/coaches.yaml`.

See [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md) for the shared seasonal workflow.

## Seasonal staff behavior

The page offers Current and Upcoming season views and opens on the current season. Its team rows come from the enabled teams in `data/seasons/<season-id>/teams.yaml`:

- Spring teams are used when that term is populated; otherwise Fall teams are used.
- Team order follows `sort_order` from the season data.
- Head-coach assignments come from the team data.
- Matching assistant coaches and reusable biographies come from `data/coaches.yaml`.

Keeping the team list season-driven prevents the Coaches page from advertising a disabled or unformed team.

## Coach photo preview

Coach photos open in a larger preview on click or tap. The preview can be closed with the close control, the backdrop, or the Escape key. The behavior lives in `assets/js/coaches.js`; its page-scoped styling belongs in `assets/css/coaches.css`.

## Styling

Keep future styling scoped to `assets/css/coaches.css`.
Avoid global overrides in `assets/css/main.css` unless the entire design system is intentionally changing.
