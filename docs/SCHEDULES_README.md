# Schedules Page Maintenance

The searchable `/schedules/` page uses local season data.

## Source files

```text
data/seasons/index.yaml
data/seasons/<season-id>/teams.yaml
data/seasons/<season-id>/schedules.yaml
layouts/partials/page-schedules.html
layouts/partials/data/schedule-events.html
assets/js/schedules.js
assets/css/schedules.css
```

For the complete season turnover workflow, see [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md).

## What appears on the page

- The season marked `current` in `data/seasons/index.yaml` supplies the visible events.
- Enabled teams from that season's `teams.yaml` supply the team tabs and sections.
- Events for disabled, archived, or upcoming teams can remain in data but are not shown in the default current-season page.
- The default all-team view shows the next two upcoming events per team.
- Selecting a team opens its complete upcoming schedule.
- Past events move into an expandable past-events area.
- Search checks teams, opponents, tournament names, locations, dates, times, and notes.
- A `?team=<team-slug>` query can open a specific team.

## Event format

Events belong under `events:` in `data/seasons/<season-id>/schedules.yaml`.

Game example:

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

Tournament example:

```yaml
events:
  - team: 13U Black
    date: 2026-07-25
    time: TBD
    type: Tournament
    title: Summer Slugfest
    location: VMP Field 4
```

## Field rules

- `team` must exactly match the team name in that season's `teams.yaml`.
- `date` must use `YYYY-MM-DD`.
- `time` may be a confirmed time or `TBD`.
- Games normally use `opponent`.
- Tournaments normally use `title`.
- `location_url`, `notes`, and `opponent` are optional.
- No event-level `status`, `enabled`, or `draft` field is currently supported. Remove or comment out an event that should not render.

Team availability is controlled in `teams.yaml`, not schedules. Setting a current-season team to `enabled: false` removes its schedule section while preserving its event data.

## Ordering

Hugo sorts events by date. Browser-side behavior separates upcoming and past events using the visitor's local date. Use real event dates so ordering and status remain predictable.

## Validation

Run:

```bash
hugo server -D --disableFastRender
```

Review `/schedules/` and check:

- all current enabled teams are present;
- disabled teams are absent;
- the first two future events appear in the all-team view;
- selecting a team reveals its full schedule;
- past events appear in the past-events area;
- search and location links work; and
- mobile layouts do not scroll horizontally.

Then run the production checks:

```bash
hugo --minify --cleanDestinationDir
bash scripts/validate-site.sh public
```
