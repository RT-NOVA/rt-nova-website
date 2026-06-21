# Accolades Overlay Banner Wall

This update changes the Banner Wall direction and leaves Current Team Results and Player Honors in the existing split-section structure.

## Banner Wall

The Banner Wall uses a realistic blank white hanging banner image:

```yaml
template: "/images/accolades/blank-white-hanging-banner.svg"
```

Dynamic items are overlaid from YAML:

```yaml
banner_wall:
  - order: 1
    year: "2026"
    season: "Spring"
    tournament: "March Mania"
    team: "13U Black"
    result: "Runner-Up"
    logo: "/images/accolades/tournament-logos/march-mania-logo.png"
    template: "/images/accolades/blank-white-hanging-banner.svg"
```

## Logo assets

Tournament logos are stored in:

```text
static/images/accolades/tournament-logos/
```

## Paging

The Banner Wall shows three banners at a time with Previous / Next controls, similar to the Social Hub pattern.

When a page has one or two remaining banners, those banners are centered.

## Existing sections

Current Team Results and Player Honors are intentionally left in their current structure.

## Accolades data model

The Accolades page uses `data/accolades.yaml` for achievements and player honors, while current-team filtering is derived from `data/teams.yaml`.

### Single source of truth for team achievements

Team tournament results now live once under `achievements:`. The Banner Wall and Current Team Results both read from that same list:

- Banner Wall: all achievements sorted by `date` descending, shown three at a time.
- Current Team Results: the same achievements, grouped by teams that are current in `data/teams.yaml`.

Do not duplicate a result in a separate `banner_wall:` section. To add a new team result, add one record under `achievements:`.

```yaml
achievements:
  - id: "2026-13u-black-march-mania-runner-up"
    date: "2026-03-15"
    year: "2026"
    season: "Spring"
    team: "13U Black"
    tournament: "March Mania"
    result: "Runner-Up"
    logo: "/images/accolades/tournament-logos/march-mania-logo.png"
    template: "/images/accolades/blank-white-hanging-banner.svg"
```

Use real event completion dates in `YYYY-MM-DD` format so sorting stays correct.

### Current teams

The Accolades page follows the same current-season logic as `/teams/`:

1. Start with `data/teams.yaml` `default_season`.
2. If a season has `status: Current`, use that season instead.
3. Read current team names from that season's `spring.teams` and `fall.teams`.

Changing the current teams in Team Central automatically controls which teams appear in Current Team Results and Player Honors.

### Player honors

Player recognition remains separate under `player_honors:` because it is a different record type than team tournament achievements.
