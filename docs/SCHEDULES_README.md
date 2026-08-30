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
- The default all-team view shows one compact accordion row per team with that team's current or next upcoming event.
- Multi-day events remain current through `end_date` and move to past events the following day.
- The page highlights events happening now or during the current/upcoming weekend above the full schedule.
- Scheduled summaries and event rows show calculated labels such as `In Progress`, `Final Day`, `Today`, `This Weekend`, `Upcoming`, and `Completed`.
- Opening an accordion reveals the team's complete upcoming schedule; only one manually opened team remains expanded at a time.
- Opening an event row reveals its notes, official tournament resources, location details, and GameChanger link when available.
- Selecting a team tab, mobile team option, or displayed team name filters to that team and opens its schedule.
- Event-type filters support `All Events`, `Tournaments`, and `Games` alongside the team and search controls. Current and weekend discovery belongs to the Now & This Weekend section rather than duplicate filter controls.
- Team Central can link directly to an expanded team schedule with `/schedules/?team=<team-slug>#team-<team-slug>`.
- Past events move into an expandable past-events area.
- Search checks teams, opponents, tournament names, locations, dates, times, and notes, then automatically opens teams containing matches.
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
    end_date: 2026-07-27
    time: TBD
    type: Tournament
    title: Summer Slugfest
    location: VMP Field 4
    info_url: https://example.com/tournament
    schedule_url: https://example.com/schedule
    standings_url: https://example.com/events/summer-slugfest/13u
    bracket_url: https://example.com/bracket
    rules_url: https://example.com/rules
```

## Field rules

- `team` must exactly match the team name in that season's `teams.yaml`.
- `date` must use `YYYY-MM-DD`.
- `end_date` is optional and must use `YYYY-MM-DD`. When omitted, the event is treated as a single-day event. Do not guess tournament end dates.
- `time` may be a confirmed time or `TBD`.
- Games normally use `opponent`.
- Tournaments normally use `title`.
- `info_url`, `schedule_url`, `standings_url`, `bracket_url`, and `rules_url` are optional tournament resource links. Only populated links appear.
- `standings_url` must open the division page for the team in that event, not the tournament's general schedule page. Store it separately on every team event because division routes vary by organizer and age group (for example, `/14u`, `/14u-open-`, or an event-specific standings URL). If the correct division page is not available yet, omit `standings_url` instead of substituting the general schedule.
- `location_url`, `notes`, and `opponent` are optional.
- No event-level `status`, `enabled`, or `draft` field is currently supported. Remove or comment out an event that should not render.

Team availability is controlled in `teams.yaml`, not schedules. Setting a current-season team to `enabled: false` removes its schedule section while preserving its event data.

## Ordering

Hugo sorts events by start date. Browser-side behavior compares the visitor's local date with `date` and `end_date` to calculate current, weekend, upcoming, and past status. Use verified event dates so ordering and status remain predictable.

## Validation

Run:

```bash
hugo server -D --disableFastRender
```

Review `/schedules/` and check:

- all current enabled teams are present;
- disabled teams are absent;
- every team accordion shows the current event before the next future event;
- a multi-day tournament remains visible through its final day and displays the full date range;
- the Now & This Weekend section contains only current or weekend events;
- event-type filters work together with team selection and search;
- opening an accordion reveals its full schedule and closes the previously opened team;
- opening an event row reveals only its populated official links and existing team GameChanger link;
- selecting a team reveals its full schedule;
- selecting a displayed team name applies the matching team filter and opens its full schedule;
- past events appear in the past-events area;
- search automatically opens matching team schedules, location links work; and
- mobile layouts do not scroll horizontally.

Then run the production checks:

```bash
hugo --minify --cleanDestinationDir
bash scripts/validate-site.sh public
```
