# Season, Team, Roster, and Schedule Maintenance

This is the primary maintenance guide for season-based website data. Use the focused guides linked below when more detail is needed.

## Source-of-truth files

```text
data/seasons/index.yaml
data/seasons/<season-id>/teams.yaml
data/seasons/<season-id>/rosters/*.yaml
data/seasons/<season-id>/schedules.yaml
data/seasons/<season-id>/tournament-results.yaml
data/seasons/<season-id>/player-honors.yaml
data/coaches.yaml
data/tryouts.yaml
```

Generated roster route files live under `content/rosters/`. Do not edit those Markdown files directly.

## Season naming and status

The season ID is the championship/spring year:

```text
2027 Season = Fall 2026 through Summer 2027
```

Add each season to `data/seasons/index.yaml`:

```yaml
- id: "2027"
  label: 2027 Season
  cycle: Fall 2026 – Summer 2027
  status: upcoming
  start_date: "2026-08-01"
  end_date: "2027-08-01"
```

Supported statuses are:

- `current`: active season used by current-team pages such as Schedules and Watch Now.
- `upcoming`: next season shown beside the current season.
- `archived`: historical season available through archives and filters.

Keep only one season marked `current`. Set `default_season` to that same season under normal circumstances.

## Team data

Teams are grouped by term in `data/seasons/<season-id>/teams.yaml`:

```yaml
spring:
  label: Spring 2027
  empty_text: Spring 2027 teams will be added as roster details are finalized.
  teams: []

fall:
  label: Fall 2026
  empty_text: Teams coming soon.
  teams:
    - name: 14U Black
      sort_order: 860
      head_coach: Chris Cheshire
      coach_role: Head Coach
      coach_photo: /images/program-media/2025_coach_cheshire_crop5.png
      record: —
      links:
        - label: Roster
          url: /rosters/2027-14u-black/
```

Supported link labels include `Roster`, `Schedule`, `GameChanger`, `Facebook`, and `Instagram`. Links are a list of `label`/`url` objects, not a keyed map.

Use `sort_order` to keep older teams first. Lower values appear first:

```text
14U Black  860
14U Orange 861
13U        872
12U        880
11U        890
10U        900
```

### Temporarily hiding a team

Add `enabled: false` to the team entry:

```yaml
- name: 11U
  enabled: false
  sort_order: 890
  head_coach: Jackson Hayes
```

When `enabled` is missing, the team is enabled. A disabled team is removed from shared seasonal team data without deleting its setup. This removes it from current/upcoming Team Central views and archives, seasonal coaching rows, current-team schedule/watch lists, and the homepage current/upcoming age-range calculation.

Historical accomplishments, news, and Social Hub posts are separate records and are intentionally preserved.

To restore the same team, change the value to `true` or remove the `enabled` field. A new team entry in a later season is enabled by default.

## Roster data and generated drafts

Create one roster data file per team and term:

```text
data/seasons/2027/rosters/14u-black.yaml
```

Example:

```yaml
team: 14U Black
season: 2027 Season
term: Fall 2026
age_group: 14U
division: Black
record: —
summary: Rawlings Tigers NOVA 14U Black upcoming roster.

players: []
staff:
  - name: Chris Cheshire
    title: Head Coach
```

After adding, renaming, disabling, enabling, or changing the `route_slug` of roster data, run:

```bash
python3 scripts/sync-roster-pages.py
```

The script generates a lightweight route file under `content/rosters/`.

### Temporarily unpublishing a roster

Set this in the roster YAML source:

```yaml
enabled: false
```

The sync script then adds this to the generated route:

```yaml
draft: true
```

Never edit `draft` directly in `content/rosters/*.md`; the next sync will replace it. `hugo server -D` includes drafts for local review, while the production build excludes the route.

To republish the roster, remove `enabled: false` or change it to `true`, then rerun the sync script.

Team and roster visibility are deliberately separate. When a team will not operate, disable both its team entry and roster source so the team is absent from listings and its direct roster route is not published.

## Schedule data

Schedule events live in `data/seasons/<season-id>/schedules.yaml`:

```yaml
events:
  - team: 13U Black
    date: 2026-07-19
    time: 12:00 PM
    type: Game
    opponent: NOVA Premier
    location: Woodbridge Middle School
    location_url: https://maps.example.com/
    notes: Optional note
```

For a tournament, use `title`:

```yaml
- team: 13U Black
  date: 2026-07-25
  time: TBD
  type: Tournament
  title: Summer Slugfest
  location: VMP Field 4
```

Important rules:

- Use `YYYY-MM-DD` dates.
- The `team` value must exactly match a team name in that season's `teams.yaml`.
- Only events from the season marked `current` are shown on `/schedules/`.
- The team list comes from enabled current-season teams. Events left in YAML for a disabled team are retained but not displayed.
- The default view shows the next two upcoming events per team. Selecting a team shows its complete schedule, and past events remain available in the past-events area.
- There is no event-level `enabled` or `draft` option. Remove or comment out an event that should not be rendered.

## Coaches

Seasonal coaching rows are created from enabled teams in `teams.yaml`. Longer bios and assistant-coach mappings live in `data/coaches.yaml`.

Disabling a team automatically removes its seasonal coaching row. Keep its `data/coaches.yaml` entry when the coaching information may be reused later.

## Tryouts and available ages

The current tryout season is maintained in `data/tryouts.yaml`.

When an age group is unavailable:

1. Update the hero `intro` and the Ages quick fact.
2. Set `enabled: false` on its `age_chart.rows` entry.
3. Remove or comment out any active `groups` schedule block for that age.

Example:

```yaml
- age_group: 11U
  enabled: false
  birth_window: May 1, 2015 – April 30, 2016
```

The age definition can remain in the file for easy restoration. Change it to `true` or remove `enabled`, restore its tryout group when applicable, and update the current-season copy when the age returns.

## Accolades and historical content

Tournament results and player honors are historical records. Do not remove them when a later-season team is disabled.

```text
data/seasons/<season-id>/tournament-results.yaml
data/seasons/<season-id>/player-honors.yaml
```

News and Social Hub posts are also independent historical content. Seasonal team availability should not rewrite past accomplishments.

## Homepage behavior

The homepage proof band calculates its current/upcoming team age range from enabled team entries. The Player Development Pathway describes the program's development philosophy and is not a promise that every age group fields a team each season. Its link sends families to Team Central for the current source of truth.

## New-season checklist

1. Add the season to `data/seasons/index.yaml` as `upcoming`.
2. Create the season directory and `teams.yaml`.
3. Add only confirmed teams. Omit `enabled`, or use `enabled: true`.
4. Create roster YAML files and run the roster sync script.
5. Add schedule events when dates are confirmed.
6. Update `data/coaches.yaml` for new bios or assistants.
7. Update `data/tryouts.yaml` for that tryout cycle and its available ages.
8. Add tournament results and player honors as the season progresses.
9. When the season turns over, change the old `current` season to `archived`, change the upcoming season to `current`, and add the next `upcoming` season.

## Validation

Use Hugo Extended 0.164.0.

```bash
python3 scripts/sync-roster-pages.py --check
hugo --minify --cleanDestinationDir
bash scripts/validate-site.sh public
```

For local review:

```bash
hugo server -D --disableFastRender
```

Check `/`, `/teams/`, `/coaches/`, `/schedules/`, `/tryouts/`, `/watch-now/`, `/accolades/`, and any new roster URLs. Remember that `-D` intentionally renders disabled roster routes marked as drafts.

## Focused guides

- [Teams](TEAMS_README.md)
- [Rosters](ROSTERS_README.md)
- [Roster sync script](ROSTER_SYNC_SCRIPT.md)
- [Schedules](SCHEDULES_README.md)
- [Tryouts](TRYOUTS_README.md)
- [Coaches](COACHES_README.md)
- [Accolades](ACCOLADES_README.md)
