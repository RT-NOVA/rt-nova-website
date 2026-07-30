# Managing Team Central

The `/teams/` page is managed from:

```text
data/seasons/<season-id>/teams.yaml
```

The page is a season-first **Team Central dashboard** for current and upcoming Rawlings Tigers NOVA teams, with a searchable season archive.

For the complete annual workflow, visibility flags, roster publishing, and related pages, start with [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md).

## Current page focus

Team Central should show:

```text
Current season
Upcoming season
Spring and Fall teams grouped under the selected season
A compact team table
A Current / Upcoming / Archive selector
A Looking for a team CTA
```

Team Central should not currently show:

```text
Large duplicate Team Central headings
Extra status badge columns
Repeated Active / Past / Upcoming badges
Heavy card layouts for each team
```

## Season model

Rawlings Tigers NOVA seasons run **fall through spring**.

Examples:

```text
2026 Season = Fall 2025 + Spring 2026
2027 Season = Fall 2026 + Spring 2027
```

The season `id` should usually match the spring year of that baseball season.

## Default season

In `data/seasons/index.yaml`, keep:

```yaml
default_season: "2026"
intro: "Explore Rawlings Tigers NOVA teams by baseball season."
```

The page should normally load the **current** season first.

The template also detects the season marked:

```yaml
status: current
```

Only one season should normally be marked `current`.

## Season statuses

Use these season-level statuses:

```text
current   The active season shown by default
upcoming  The next season shown in the toggle
archived  Historical seasons available through archive search
```

Recommended setup:

```yaml
seasons:
  - id: "2026"
    label: "2026 Season"
    cycle: "Fall 2025 – Spring 2026"
    status: current

  - id: "2027"
    label: "2027 Season"
    cycle: "Fall 2026 – Spring 2027"
    status: upcoming
```

## Current / Upcoming / Archive selector

The Team Central page uses season buttons plus Archive:

```text
Current 2026 Season | Upcoming 2027 Season | Archive
```

Current and upcoming buttons show their team counts. Archive opens season, team, and search filters without rendering every historical season at once.

## Season header copy

The black season header should remain simple:

```text
2026 Season
Fall 2025 – Spring 2026
Choose a season to view active and upcoming Rawlings Tigers NOVA teams.
```

Avoid repeating this copy in multiple places. Do not include duplicate helper lines such as:

```text
Seasons run fall through spring.
Spring and fall teams are grouped together under one baseball season.
```

The fall-through-spring rule can be explained in this README, and optionally once in a short helper line on the page if needed.

## Spring and Fall sections

Each season can have:

```yaml
spring:
fall:
```

Spring should appear first when it exists.

Example:

```yaml
spring:
  label: "Spring 2026"
  teams:
    - name: "13U Black"
      head_coach: "Chris Cheshire"
      coach_role: "Head Coach"
      coach_photo: "/images/program-media/2025_coach_cheshire_crop5.png"
      record: "—"
      sort_order: 870
      links:
        - label: Roster
          url: /rosters/2026-13u-black/
fall:
  label: "Fall 2025"
  teams: []
```

## Coming soon sections

If a term does not have team details yet, keep the message simple and avoid implying that coaches are not set.

Recommended wording:

```yaml
spring:
  label: "Spring 2027"
  empty_text: "Coming soon. Additional Spring 2027 team details will be posted as they are available."
  teams: []
```

Avoid wording like:

```text
teams will be added once rosters, coaches, and schedules are finalized
```

That can make it sound like the program is waiting on coaches.

## Team table columns

The current Team Central table should use four columns:

```text
Team | Head Coach | Record | Team Links
```

Do not add a Status column. The selected season and Spring/Fall headings already provide enough context.

## Team row fields

Each team should include:

```yaml
- name: "14U Black"
  sort_order: 860
  head_coach: "Chris Cheshire"
  coach_role: "Head Coach"
  coach_photo: "/images/program-media/2025_coach_cheshire_crop5.png"
  record: "—"
  links:
    - label: Roster
      url: /rosters/2027-14u-black/
```

Blank links are okay. The page should show available links and avoid broken buttons.

`enabled` is optional and defaults to `true`. Set it to `false` to retain a team configuration without showing it in shared seasonal listings:

```yaml
- name: 11U
  enabled: false
  sort_order: 890
  head_coach: Jackson Hayes
```

Disabling a team also removes it from seasonal coaching rows, current-team Schedule/Watch lists, and the homepage current/upcoming age range. It does not delete historical news or accomplishments. Disable the corresponding roster source separately when its direct route should also be unpublished.

## Team sort order

Teams should sort with older age groups first.

For the same age group, **Black** should appear before **Orange**.

Recommended `sort_order` values:

```text
14U Black    860
14U Orange   861
13U Black    870
13U Orange   871
13U          872
12U          880
11U          890
10U          900
```

Lower numbers appear first.

Examples:

```yaml
sort_order: 860  # 14U Black
sort_order: 861  # 14U Orange
sort_order: 870  # 13U Black
sort_order: 871  # 13U Orange
sort_order: 890  # 11U
```

## Team links

Supported link labels:

```yaml
links:
  - label: Facebook
    url: https://www.facebook.com/example
  - label: Instagram
    url: https://www.instagram.com/example
  - label: Roster
    url: /rosters/2027-14u-black/
  - label: Schedule
    url: /schedules/?team=14u-black#team-14u-black
  - label: GameChanger
    url: https://web.gc.com/teams/example/team
```

The label controls the compact icon used in Team Central:

```text
Roster       people icon and orange roster link
Schedule     calendar icon
GameChanger  GC mark
Facebook     Facebook icon
Instagram    Instagram icon
```

Use these exact labels so the intended icon and accessible text are rendered. A missing or placeholder URL is displayed as unavailable rather than as a broken link.

Current-team schedule links should include both the `team` query value and matching `team-<slug>` anchor. The query selects and expands that team's schedule, while the anchor moves the visitor directly to the expanded team section. Do not use legacy `/leagues/team/` schedule URLs.

Use full URLs for outside sites:

```yaml
- label: Facebook
  url: "https://www.facebook.com/..."
```

Use root-relative URLs for local pages:

```yaml
- label: Roster
  url: "/rosters/2027-13u-black/"
```

## Coach images

Coach images should be stored under:

```text
static/images/program-media/
```

Reference them with root-relative paths:

```yaml
coach_photo: "/images/program-media/2025_coach_cheshire_crop5.png"
```

Use square or near-square crops when possible. Keep file sizes web-friendly.

## Updating seasons each year

When the next season becomes active, update the season statuses.

Before:

```yaml
- id: "2026"
  status: current
- id: "2027"
  status: upcoming
```

After:

```yaml
- id: "2026"
  status: archived
- id: "2027"
  status: current
- id: "2028"
  status: upcoming
```

Then update `default_season` in `data/seasons/index.yaml`:

```yaml
default_season: "2027"
```

## Visual requirements

Keep the page cohesive and avoid making it feel like separate disconnected sections.

Current design direction:

```text
Dark hero
One black season dashboard header
Current / Upcoming toggle inside the black header
Spring and Fall subsections inside the same dashboard flow
Banded table rows for readability
No extra status badges
Searchable Archive selector for historical teams
```

Mobile/tablet requirements:

```text
No horizontal scrolling
Toggle stacks cleanly if needed
Table rows become readable stacked panels on small screens
Team links wrap naturally
Coach images stay small
Spacing between Spring and Fall sections remains compact
```

## Local testing

After editing `data/seasons/<season-id>/teams.yaml`, run:

```bash
hugo server -D
```

Then check:

```text
/teams/
```

Test at these widths:

```text
390px phone
430px large phone
768px tablet portrait
1024px tablet landscape
1280px desktop
```

## Troubleshooting

### Hugo fails after a data edit

Do not leave backup files inside `data/`.

Bad:

```text
data/seasons/<season-id>/teams.yaml.bak-teamcentral-selector-cleanup
```

Hugo tries to load files in `data/` and will fail on unknown backup extensions.

Move backup files outside Hugo-managed folders or rely on Git history instead.

### Toggle shows a white cap above the season header

The Current / Upcoming toggle must be inside the black season header in:

```text
layouts/partials/page-teams.html
```

Do not render a separate white Select Season header around the toggle.

### Team order is wrong

Check `sort_order` values. Lower numbers appear first.

## Team Central archive search

The Team Central page includes an `Archive` selector option alongside the current/upcoming season buttons. The existing current/upcoming team views remain unchanged. Selecting `Archive` opens a searchable team browser.

Archive filters:

- `Season`: Defaults to `Current Season` and then lists individual seasons from `data/seasons/index.yaml`. The archive intentionally does not include an `All Seasons` option so the page does not render every historical team at once as the archive grows.
- `Team`: Updates based on the selected season and lists only teams from that season.
- `Search`: Matches team name, coach name, coach role, season label/year/status, and spring/fall term label within the selected season.

Team data still comes from `data/seasons/<year>/teams.yaml`. Spring and fall are shown as supporting context inside archive results, but the archive remains season-first for clearer browsing and better long-term performance.
