# Managing Team Central

The `/teams/` page is managed from:

```text
data/teams.yaml
```

The page is intended to be a clean **Team Central dashboard** for current and upcoming Rawlings Tigers NOVA teams. It should stay focused on active and upcoming teams only. Older team history can be handled later with a separate archive solution.

## Current page focus

Team Central should show:

```text
Current season
Upcoming season
Spring and Fall teams grouped under the selected season
A compact team table
A Current / Upcoming toggle
A Looking for a team CTA
```

Team Central should not currently show:

```text
Past season archive cards
Large duplicate Team Central headings
Extra status badge columns
Repeated Active / Past / Upcoming badges
Heavy card layouts for each team
```

## Season model

Rawlings Tigers NOVA seasons run **fall through spring**.

Examples:

```text
2026 Season = Fall 2025 + Spring 2026
2027 Season = Fall 2026 + Spring 2027
```

The season `id` should usually match the spring year of that baseball season.

## Default season

At the top of `data/teams.yaml`, keep:

```yaml
default_season: "2026"
intro: "Explore Rawlings Tigers NOVA teams by baseball season."
```

The page should normally load the **current** season first.

The template also detects the season marked:

```yaml
status: current
```

Only one season should normally be marked `current`.

## Season statuses

Use these season-level statuses:

```text
current   The active season shown by default
upcoming  The next season shown in the toggle
past      Older seasons, not shown on the main Team Central page for now
```

Recommended setup:

```yaml
seasons:
  - id: "2026"
    label: "2026 Season"
    cycle: "Fall 2025 – Spring 2026"
    status: current

  - id: "2027"
    label: "2027 Season"
    cycle: "Fall 2026 – Spring 2027"
    status: upcoming
```

## Current / Upcoming toggle

The Team Central page uses a two-option toggle:

```text
Upcoming 2027 Season | Current 2026 Season
```

The toggle should live inside the black season header area, inline with the selected season heading. Do not reintroduce a separate white “Select Season” header/card above the black season header.

## Season header copy

The black season header should remain simple:

```text
2026 Season
Fall 2025 – Spring 2026
Choose a season to view active and upcoming Rawlings Tigers NOVA teams.
```

Avoid repeating this copy in multiple places. Do not include duplicate helper lines such as:

```text
Seasons run fall through spring.
Spring and fall teams are grouped together under one baseball season.
```

The fall-through-spring rule can be explained in this README, and optionally once in a short helper line on the page if needed.

## Spring and Fall sections

Each season can have:

```yaml
spring:
fall:
```

Spring should appear first when it exists.

Example:

```yaml
spring:
  label: "Spring 2026"
  teams:
    - name: "13U Black"
      age: 13
      division: "Black"
      coach: "Chris Cheshire"
      coach_title: "Head Coach"
      coach_image: "/images/coaches/chris-cheshire.jpg"
      record: "—"
      sort_order: 870
      links:
        facebook: ""
        instagram: ""
        roster: ""
        schedule: ""
        gamechanger: ""
fall:
  label: "Fall 2025"
  teams: []
```

## Coming soon sections

If a term does not have team details yet, keep the message simple and avoid implying that coaches are not set.

Recommended wording:

```yaml
spring:
  label: "Spring 2027"
  message: "Coming soon. Additional Spring 2027 team details will be posted as they are available."
  teams: []
```

Avoid wording like:

```text
teams will be added once rosters, coaches, and schedules are finalized
```

That can make it sound like the program is waiting on coaches.

## Team table columns

The current Team Central table should use four columns:

```text
Team | Head Coach | Record | Team Links
```

Do not add a Status column. The selected season and Spring/Fall headings already provide enough context.

## Team row fields

Each team should include:

```yaml
- name: "14U Black"
  age: 14
  division: "Black"
  coach: "Chris Cheshire"
  coach_title: "Head Coach"
  coach_image: "/images/coaches/chris-cheshire.jpg"
  record: "—"
  sort_order: 860
  links:
    facebook: ""
    instagram: ""
    roster: ""
    schedule: ""
    gamechanger: ""
```

Blank links are okay. The page should show available links and avoid broken buttons.

## Team sort order

Teams should sort with older age groups first.

For the same age group, **Black** should appear before **Orange**.

Recommended `sort_order` values:

```text
14U Black    860
14U Orange   861
13U Black    870
13U Orange   871
13U          872
12U          880
11U          890
10U          900
```

Lower numbers appear first.

Examples:

```yaml
sort_order: 860  # 14U Black
sort_order: 861  # 14U Orange
sort_order: 870  # 13U Black
sort_order: 871  # 13U Orange
sort_order: 890  # 11U
```

## Team links

Supported link keys:

```yaml
links:
  facebook: ""
  instagram: ""
  roster: ""
  schedule: ""
  gamechanger: ""
```

Use full URLs for outside sites:

```yaml
facebook: "https://www.facebook.com/..."
```

Use root-relative URLs for local pages:

```yaml
roster: "/teams/13u-black/roster/"
schedule: "/teams/13u-black/schedule/"
```

## Coach images

Coach images should be stored under:

```text
static/images/coaches/
```

Reference them with root-relative paths:

```yaml
coach_image: "/images/coaches/chris-cheshire.jpg"
```

Use square or near-square crops when possible. Keep file sizes web-friendly.

## Updating seasons each year

When the next season becomes active, update the season statuses.

Before:

```yaml
- id: "2026"
  status: current
- id: "2027"
  status: upcoming
```

After:

```yaml
- id: "2026"
  status: past
- id: "2027"
  status: current
- id: "2028"
  status: upcoming
```

Then update:

```yaml
default_season: "2027"
```

## Visual requirements

Keep the page cohesive and avoid making it feel like separate disconnected sections.

Current design direction:

```text
Dark hero
One black season dashboard header
Current / Upcoming toggle inside the black header
Spring and Fall subsections inside the same dashboard flow
Banded table rows for readability
No extra status badges
No archive section on the main /teams/ page for now
```

Mobile/tablet requirements:

```text
No horizontal scrolling
Toggle stacks cleanly if needed
Table rows become readable stacked panels on small screens
Team links wrap naturally
Coach images stay small
Spacing between Spring and Fall sections remains compact
```

## Local testing

After editing `data/teams.yaml`, run:

```bash
hugo server -D
```

Then check:

```text
/teams/
```

Test at these widths:

```text
390px phone
430px large phone
768px tablet portrait
1024px tablet landscape
1280px desktop
```

## Troubleshooting

### Hugo fails after applying a patch

Do not leave backup files inside `data/`.

Bad:

```text
data/teams.yaml.bak-teamcentral-selector-cleanup
```

Hugo tries to load files in `data/` and will fail on unknown backup extensions.

Move backups outside Hugo-managed folders:

```bash
mkdir -p .backups
find data -type f \( -name "*.bak*" -o -name "*backup*" \) -exec mv {} .backups/ \;
```

### Toggle shows a white cap above the season header

The Current / Upcoming toggle must be inside the black season header in:

```text
layouts/partials/page-teams.html
```

Do not render a separate white Select Season header around the toggle.

### Team order is wrong

Check `sort_order` values. Lower numbers appear first.
