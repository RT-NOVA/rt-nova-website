# Season Data Split

This refactor splits season-based data into official baseball-season folders.

## Season naming

Season IDs use the baseball/championship season year, not the calendar range.

Example:

- `2026` = the 2026 Season
- The 2026 Season began on August 12, 2025
- The 2026 Season runs through late July / early August 2026

## Season index

`data/seasons/index.yaml` controls season order and status.

```yaml
default_season: "2026"
seasons:
  - id: "2027"
    label: "2027 Season"
    cycle: "Fall 2026 – Summer 2027"
    status: "upcoming"

  - id: "2026"
    label: "2026 Season"
    cycle: "August 12, 2025 – early August 2026"
    status: "current"
```

Supported statuses:

- `current`
- `upcoming`
- `archived`

## Split files

Each season can now carry its own data:

```text
data/seasons/
  index.yaml
  2026/
    teams.yaml
    schedules.yaml
    tournament-results.yaml
    player-honors.yaml
  2027/
    teams.yaml
    schedules.yaml
    tournament-results.yaml
    player-honors.yaml
```

## Page behavior

- `/teams/` shows current and upcoming seasons.
- `/schedules/` shows current teams by default and reads local schedule data from season folders.
- `/accolades/` combines tournament results and player honors across season folders, while still defaulting around current-team behavior.
- Roster pages use the split team data to find records.

## Deprecated aggregate files

These aggregate files are retained only as compatibility/deprecation pointers:

- `data/teams.yaml`
- `data/schedules.yaml`
- `data/accolades.yaml`

Do not add new seasonal data there.
