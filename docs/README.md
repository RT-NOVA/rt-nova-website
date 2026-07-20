# Website documentation

This is the starting point for maintaining the Rawlings Tigers NOVA website. The guides below describe the current site, not a history of redesign patches.

## Start here

| Need | Guide |
|---|---|
| Start a new season, publish or hide a team, and coordinate related pages | [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md) |
| Change a page layout, component, stylesheet, or browser behavior | [`FRONTEND_MAINTENANCE.md`](FRONTEND_MAINTENANCE.md) |
| Understand the page rhythm and color system | [`PAGE_FLOW_REFERENCE.md`](PAGE_FLOW_REFERENCE.md) and [`section-color-pattern.md`](section-color-pattern.md) |

## Teams and seasonal operations

| Area | Guide |
|---|---|
| Team Central, team visibility, sorting, and team links | [`TEAMS_README.md`](TEAMS_README.md) |
| Roster data and publishing | [`ROSTERS_README.md`](ROSTERS_README.md) |
| Generated roster routes and sync checks | [`ROSTER_SYNC_SCRIPT.md`](ROSTER_SYNC_SCRIPT.md) |
| Schedules and GameChanger links | [`SCHEDULES_README.md`](SCHEDULES_README.md) |
| Tryout dates, age availability, and FAQs | [`TRYOUTS_README.md`](TRYOUTS_README.md) |
| Coaches and seasonal staff | [`COACHES_README.md`](COACHES_README.md) |
| Accolades, player honors, and homepage achievement images | [`ACCOLADES_README.md`](ACCOLADES_README.md) |

## Program pages and content

| Area | Guide |
|---|---|
| Homepage images and media fields | [`HOMEPAGE_MEDIA.md`](HOMEPAGE_MEDIA.md) |
| Social Hub content and behavior | [`SOCIAL_HUB_README.md`](SOCIAL_HUB_README.md) |
| Social images and helper tooling | [`SOCIAL_HUB_IMAGES.md`](SOCIAL_HUB_IMAGES.md) and [`SOCIAL_IMAGE_HELPERS.md`](SOCIAL_IMAGE_HELPERS.md) |
| News posts | [`NEWS_README.md`](NEWS_README.md) |
| Watch Now | [`WATCH_NOW_README.md`](WATCH_NOW_README.md) |
| Training locations | [`TRAINING_LOCATIONS_README.md`](TRAINING_LOCATIONS_README.md) |
| Family Hub | [`FAMILY_HUB_README.md`](FAMILY_HUB_README.md) |
| Booster Club | [`BOOSTER_CLUB_README.md`](BOOSTER_CLUB_README.md) |
| Sponsorship opportunities | [`SPONSORSHIP_OPPORTUNITIES_README.md`](SPONSORSHIP_OPPORTUNITIES_README.md) |
| Coaching opportunities | [`COACHING_OPPORTUNITIES_README.md`](COACHING_OPPORTUNITIES_README.md) |
| Coaching registration | [`COACHING_REGISTRATION_README.md`](COACHING_REGISTRATION_README.md) |
| Shared FAQ data | [`SHARED_FAQ_README.md`](SHARED_FAQ_README.md) |
| SEO and search metadata | [`SEO_README.md`](SEO_README.md) |

## Design and technical references

| Area | Guide |
|---|---|
| Header, navigation, and dropdowns | [`header-navigation.md`](header-navigation.md) |
| CSS/JavaScript ownership and validation | [`FRONTEND_MAINTENANCE.md`](FRONTEND_MAINTENANCE.md) |
| Page flow and section rhythm | [`PAGE_FLOW_REFERENCE.md`](PAGE_FLOW_REFERENCE.md) |
| Section color roles | [`section-color-pattern.md`](section-color-pattern.md) |
| Accolade banner markup reference | [`ACCOLADES_BANNER_TEMPLATE.html`](ACCOLADES_BANNER_TEMPLATE.html) |

## Maintenance rules

- Edit source data, templates, and assets rather than generated files in `public/`.
- Preserve unrelated working-tree changes.
- Keep changes scoped to the requested page or component.
- Use Hugo Extended `0.164.0`, matching local and Cloudflare builds.
- Run the validation commands in [`FRONTEND_MAINTENANCE.md`](FRONTEND_MAINTENANCE.md) after updates.
- Historical implementation notes are kept in Git history rather than as active maintenance guides.
