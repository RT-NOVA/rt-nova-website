# Team Central Markdown/Data Workflow

The `/teams/` page is driven by `data/teams.yaml` and rendered by `layouts/partials/page-teams.html`.

## Season model

Rawlings Tigers NOVA seasons run from fall through the following spring:

- `2026 Season` = Fall 2025 + Spring 2026
- `2027 Season` = Fall 2026 + Spring 2027

Spring is displayed first inside each season because spring is the primary active season when rosters/schedules are live.

## Current and upcoming teams

Use `seasons:` for current/upcoming seasons shown in the main selector.

Each season has:

```yaml
- id: "2027"
  label: "2027 Season"
  cycle: "Fall 2026 – Spring 2027"
  status: "Upcoming"
  summary: "..."
  spring:
    label: "Spring 2027"
    status: "Coming Soon"
    empty_text: "Spring 2027 teams will be added once rosters, coaches, and schedules are finalized."
    teams: []
  fall:
    label: "Fall 2026"
    status: "Upcoming"
    teams:
      - name: "13U"
        status: "Upcoming"
        head_coach: "Jose Acosta"
        coach_role: "Head Coach"
        coach_photo: "/images/teamlinkt/jose-acosta-temp.jpg"
        record: "—"
        links: []
```

## Past seasons

Use `past_seasons:` for archived seasons. These are hidden behind the Past Seasons expander so the Team Central page stays focused on current/upcoming teams.

## Team links

Common links:

```yaml
links:
  - label: "Roster"
    url: "https://..."
  - label: "Schedule"
    url: "https://..."
  - label: "GameChanger"
    url: "https://..."
  - label: "Instagram"
    url: "https://..."
  - label: "Facebook"
    url: "https://..."
```
