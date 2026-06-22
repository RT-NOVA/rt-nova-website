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

### Current Team Results carousel

Current Team Results now stays compact. Each current-team card shows up to three achievements at a time and uses small text-only Previous / Next controls when a team has more than three matching results. The controls page within that team card only; they do not expand the card vertically.

Tournament images in this section use the `logo` field from each achievement and are displayed as centered logo artwork, not as banner previews. The Banner Wall remains the visual banner showcase.

### Searching past team achievements from Current Team Results

The team dropdown remains limited to current teams from `data/teams.yaml`, but the search box can now match any record in `achievements:`. When the search field is empty, the section shows current teams only. When a search term is entered, matching older teams/results can appear temporarily in the results area without being added to the dropdown.

### Player Honors grouped by team

Player Honors are now grouped by current team, with player-first cards inside each team group. Each card uses the honor graphic as a supporting thumbnail and leads with the player name. Team groups show up to three honors at a time and use compact Previous / Next controls when more honors are available.

`player_honors:` supports optional `player:` and `honor:` fields. If those are missing, the template falls back to the existing `title:` value.

### Player Honors vertical card treatment

Player Honors now use a more visual recognition-card style inside each team group: larger centered thumbnails, player name as the primary text, and honor/year metadata below the name. This keeps team grouping and carousel behavior while making the individual recognitions feel less like table rows.

### Player Honors free grid behavior

Player Honors no longer use team group containers. The default view shows up to the first three honors for each current team in one free-flowing grid. Selecting a team shows all honors for that team. Typing in search shows all matching honors. This keeps the section lighter while still supporting team and player filtering.

### Team Results & History section copy

The Team Accolades section heading now reads `Team Results & History` because the dropdown remains focused on current teams while the search field can surface older tournament achievements from the full `achievements:` list.

### Tournament Results section copy

The Team Accolades section now uses the heading `Tournament Results` with supporting copy: `Browse current teams or search past tournament accomplishments.`

### Team order and softer filters

Team dropdowns now sort older age groups first, such as 13U before 10U, and the JavaScript uses the same ordering for Team Results and Player Honors filter options. Filter/search panels have also been softened with lighter translucent backgrounds and underline-style inputs so they blend better with the page.

### Older-age team display order

Team Results sections and Player Honors cards are reordered client-side so older age groups display first on the page, matching the filter dropdown order.

### Year-based season filtering

Tournament Results and Player Honors use year-based season filters from `data/seasons/index.yaml`:

- `Current Season`
- `All Seasons`
- Individual season labels such as `2026 Season` and `2025 Season`

Filtering is based on `season_id + team`. Spring and Fall terms may still appear on individual cards, but they are not used as top-level visible grouping or filter categories.

When `All Seasons` is selected, repeated team names are disambiguated in the Team dropdown with the season label, such as `13U Black — 2026 Season`.
