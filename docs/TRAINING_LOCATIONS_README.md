# Training Locations page

The `/training-locations/` page is driven by `data/training_locations.yaml`.

## Files

- `data/training_locations.yaml`
- `layouts/partials/page-training-locations.html`
- the matching route stylesheet in `assets/css/`
- facility images in `static/images/training-locations/`

## Page data

The data file contains:

```text
intro                 page introduction
proof                 quick facts beneath the hero
expectation            parent-planning section and feature items
outdoor.locations      outdoor field cards
winter.locations       indoor facility cards
faq.items              common location questions
cta                    final next actions
```

## Adding or updating a location

Outdoor and winter locations share these common fields:

```yaml
- name: Veterans Memorial Park
  field: Field 4
  area: Woodbridge, VA
  address: 14300 Veterans Dr, Woodbridge, VA 22191
  use: Outdoor practices, tryouts, team workouts, and baseball development sessions
  season: Spring / Summer / Fall
  note: Primary Woodbridge outdoor field location when permits and team schedules align.
  map_url: https://www.google.com/maps/search/?api=1&query=...
```

Winter facilities may also include:

```yaml
logo: /images/training-locations/dbat-logo.webp
website_url: https://www.example.com/
```

Use a site-root path for local logos. Confirm map and facility links after changing them.

## Current location groups

The page currently documents:

- Veterans Memorial Park, Field 4
- Eagle Field at Neabsco
- Dale City Recreation Center / Community Park, Baseball Field 2
- D-BAT Manassas
- Metro Baseball Facility
- Veterans Community Center

Location details can vary by team, permits, season, and weather. Keep that qualification in the parent-planning and FAQ copy rather than promising a permanent assignment.

## Related homepage content

The homepage Local Roots section is only a short teaser. When locations change, review both `data/training_locations.yaml` and `why.local` in `data/homepage.yaml`, but keep the homepage copy concise and link visitors here for the details.
