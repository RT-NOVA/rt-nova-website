# Rosters

Roster data is maintained in season-based YAML files. Markdown files under `content/rosters/` are generated route stubs and should not be edited by hand.

## Source of truth

Use one roster data file per team and term:

```text
data/seasons/<season-id>/rosters/<team-key>.yaml
```

Examples:

```text
data/seasons/2026/rosters/11u.yaml
data/seasons/2026/rosters/11u-fall.yaml
data/seasons/2026/rosters/13u-orange.yaml
```

## Spring and fall roster pages

Players can change between fall and spring. Use separate roster YAML files when the team has separate fall and spring rosters.

Example:

```text
data/seasons/2026/rosters/11u.yaml       # Spring 2026
data/seasons/2026/rosters/11u-fall.yaml  # Fall 2025
```

The spring roster can keep the existing public URL by setting:

```yaml
route_slug: "2026-11u"
```

The fall roster can use:

```yaml
route_slug: "2026-11u-fall"
```

That generates:

```text
/rosters/2026-11u/
/rosters/2026-11u-fall/
```

## Roster data format

```yaml
team: "11U"
route_slug: "2026-11u"
page_date: "2026-06-16"
season: "2026 Season"
term: "Spring 2026"
age_group: "11U"
division: ""
record: "—"
summary: "Rawlings Tigers NOVA 11U spring roster."

players:
  - number: "2"
    name: "Logan Moore"
    positions: "P, 3B, OF"

staff:
  - name: "Ken Torres"
    title: "Head Coach"
```

The roster template renders head coaches before assistant coaches in the Coaching Staff table.

## Generate roster pages

After adding a new roster YAML, renaming a roster YAML, deleting a generated roster page, or changing `route_slug`, run:

```bash
python3 scripts/sync-roster-pages.py
```

Then run Hugo:

```bash
hugo server -D --disableFastRender
```

Normal player/staff edits in an existing roster YAML do not require the sync script.

## Check generated files

```bash
python3 scripts/sync-roster-pages.py --check
```

## Layout

Roster pages render as open, line-based tables:

- Roster: `#`, `Name`, `Positions`
- Coaching Staff: `Name`, `Title`

Player and staff photo fields are intentionally not used by the roster page.


## Fall 2025 roster data source note

The Fall 2025 11U, 13U Black, and 13U Orange roster YAML files were created from legacy site screenshots.

The 13U Orange screenshot did not show player positions or staff, so those fields are intentionally blank until confirmed.
