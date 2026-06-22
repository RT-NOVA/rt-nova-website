# Schedules Page

Adds a searchable `/schedules/` page using local data only.

## Files

- `content/schedules.md`
- `layouts/partials/page-schedules.html`
- `assets/css/schedules.css`
- `data/schedules.yaml`
- `layouts/_default/single.html`

## Behavior

- Current teams are determined from `data/teams.yaml`.
- Current teams are shown by default.
- The team dropdown includes current teams only.
- Older age groups sort first on the page and in the dropdown.
- Search can find team names, opponents, locations, and event titles from local schedule data.
- Each team shows up to three game/tournament entries by default.
- Selecting a team or searching can reveal additional matching events.
- No Roster, GameChanger, legacy site, or other external schedule links are rendered.

## Local schedule data

Schedule events live in `data/schedules.yaml`.

Supported event fields:

```yaml
events:
  - team: 13U Black
    date: 2026-06-28
    time: 9:00 AM
    type: Game
    opponent: Stars Baseball
    location: VMP Field 4
    notes: Optional note
```

For tournaments, use `title` instead of `opponent`:

```yaml
events:
  - team: 13U Black
    date: 2026-07-06
    type: Tournament
    title: Summer Showdown
    location: TBD
```

No `status` field is needed in schedule events. Current team status comes from `data/teams.yaml`.

## v3 team order fix

Fixed the JavaScript age-group sort regex so teams correctly sort older-first on the page and in the dropdown. Example order: `13U Black`, `13U Orange`, `11U`, `10U`.

## v4 sample schedule data

Added seven sample game/tournament entries for each current team: `13U Black`, `13U Orange`, `11U`, and `10U`. These are placeholder examples for layout testing and should be replaced with confirmed schedule details before production use.

## v5 search fix

Fixed Schedule page search so it searches both team metadata and local event details. Search now matches team names, opponents, event titles, locations, dates, and times. When a team name matches, the matching team section shows its events instead of hiding them behind the default three-item behavior.

## v6 tournament label fix

Tournament events no longer prepend `vs` when an `opponent` field is present. Games still render opponents as `vs Opponent`, while tournaments render the event/opponent text directly.

## v7 default event limit and expansion

Each team now shows only the first three schedule entries by default. Teams with more than three entries display a `Show all` button below the visible entries; clicking it expands that team only and clicking again collapses it back to three. Search results are not limited to three so matching entries can be found.


## Season data split

Schedule events now live under `data/seasons/<season-id>/schedules.yaml`.

## v8 schedules dispatch fix

Fixed `/schedules/` rendering after later patches overwrote `layouts/_default/single.html` without the schedules template dispatch. The page now routes `template: schedules` to `layouts/partials/page-schedules.html` again.
