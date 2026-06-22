# Rosters

Roster pages use lightweight markdown route files and season-based YAML data.

## Route files

Roster page URLs remain under:

```text
content/rosters/
```

Each markdown file should only identify the season and roster key:

```yaml
---
title: "2026 13U Orange Roster"
date: 2026-06-16
season_id: "2026"
roster_key: "13u-orange"
summary: "Rawlings Tigers NOVA 13U Orange spring roster."
---
Rawlings Tigers NOVA 13U Orange spring roster.
```

## Roster data files

Roster data lives under each season:

```text
data/seasons/2026/rosters/13u-orange.yaml
```

Use one YAML file per team so roster edits stay small and reviewable.

## Player format

```yaml
players:
  - number: "45"
    name: "Cameron Branham"
    positions: "P, 1B, OF"
```

## Staff format

```yaml
staff:
  - name: "Tim Jacoby"
    title: "Head Coach"
  - name: "Don Yizar"
    title: "Assistant Coach"
```

The roster template renders head coaches before assistant coaches in the Coaching Staff table.

## Layout

Roster pages render as open, line-based tables:

- Roster: `#`, `Name`, `Positions`
- Coaching Staff: `Name`, `Title`

Player and staff photo fields are intentionally not used by the roster page.
