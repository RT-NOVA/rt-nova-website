# Accolades Page

The Accolades page combines featured stories, searchable team banners, and a rotating Hall of Recognition.

## Data sources

Season-specific content lives in:

```text
data/seasons/<season-id>/tournament-results.yaml
data/seasons/<season-id>/player-honors.yaml
```

Current-season and current-team status comes from `data/seasons/index.yaml` and `data/seasons/<season-id>/teams.yaml`, using the same rules as Team Central.

Accolades are historical records. Disabling a later-season team with `enabled: false` does not remove earlier tournament results, player honors, news stories, or Social Hub posts.

## Team accolades

Tournament results belong under `achievements:` in the appropriate `tournament-results.yaml` file.

```yaml
achievements:
  - id: 2026-13u-black-cap-city-showdown-runner-up
    date: "2026-04-11"
    year: "2026"
    season: Spring
    team: 13U Black
    tournament: USSSA Cap City Showdown
    result: Runner-Up
    logo: /images/accolades/tournament-logos/cap-city-showdown-logo.png
    template: /images/accolades/blank-white-hanging-banner.svg
    story_url: /news/example-story/
```

Use a real event completion `date` in `YYYY-MM-DD` format. Team Accolades uses that field to sort tournament results newest first.

Tournament logos are stored in `static/images/accolades/tournament-logos/`. The default hanging-banner artwork is `static/images/accolades/blank-white-hanging-banner.svg`.

Tournament logos use the shared banner position by default. When artwork has unusual internal padding, add `logo_position_y` (for example, `47%`) to adjust that achievement vertically without resizing the logo or affecting other banners.

The searchable banner gallery defaults to All Seasons and shows three matching banners per page. Filters support season, team, tournament, result, and free-text searching.

## Manually selecting Featured Achievements

Featured Achievements normally displays the newest three eligible tournament stories. Add `featured: true` to an achievement when it should receive manual priority.

```yaml
achievements:
  - id: 2026-13u-black-cap-city-showdown-runner-up
    date: "2026-04-11"
    year: "2026"
    season: Spring
    team: 13U Black
    tournament: USSSA Cap City Showdown
    result: Runner-Up
    logo: /images/accolades/tournament-logos/cap-city-showdown-logo.png
    story_url: /news/2026-04-13-example-story/
    featured: true
```

Selection behavior:

1. An achievement is eligible only when it has a `story_url` or `social_url` and a usable image.
2. A direct `feature_image` may be provided. Otherwise, the image, title, summary, and alternate text are inherited from the linked local news or Social Hub page when available.
3. If one or more eligible achievements use `featured: true`, those items are placed first, newest date first.
4. If fewer than three eligible items are manually featured, the remaining slots are filled with the newest eligible unmarked achievements.
5. If nothing is marked `featured: true`, the page automatically displays the newest three eligible achievements. This preserves the normal page behavior without requiring manual labels.
6. If more than three items are marked, the newest three marked items are displayed.
7. A marked item without a destination link or usable image is ignored and does not create a broken card.

The homepage recruiting section uses the same three selected Featured Achievements as its image pool. The newest selected achievement appears first, then the section crossfades through the remaining images every 4.5 seconds.

Optional fields:

- `feature_image`: overrides the image inherited from the linked page.
- `story_label`: overrides `Read the story` or `View the post`.
- `feature_crop`: retains compatibility with existing content metadata, although Featured Achievement images are displayed without cropping by default.

## Hall of Recognition

Player recognition belongs under `player_honors:` in the appropriate `player-honors.yaml` file.

```yaml
player_honors:
  - id: 2026-13u-black-player-name-player-highlight
    year: "2026"
    team: 13U Black
    title: Player Name 2026 Player Highlight
    image: /images/program-media/player-name-2026-01.png
    player: Player Name
    honor: Player Highlight
```

Player Honors are intentionally organized by the latest season/year, not by exact dates. Do not add honor dates solely for display ordering.

The Hall of Recognition:

- defaults to All Seasons;
- shows six portraits at a time;
- prioritizes the newest season and term;
- balances the default selection across teams with available honors;
- may rotate the specific players shown when the page reloads;
- keeps filtered and searched results predictable; and
- opens portraits in a larger image preview.

## Empty filter results

Team Accolades and Hall of Recognition provide contextual empty messages. A search with no matches offers Clear Filters, while a season with no posted content offers View All Seasons.

## Display order

When team names need ordering, older age groups appear first. For teams of the same age, Black appears before Orange.
