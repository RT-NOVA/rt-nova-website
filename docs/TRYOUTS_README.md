# Tryouts Page Maintenance

The Tryouts page is rendered from:

```text
data/tryouts.yaml
layouts/partials/page-tryouts.html
assets/css/tryouts.css
```

## Current page behavior

The page combines the published age chart and scheduled `groups` into one age-group selector:

- The all-ages view shows only real published evaluation sessions.
- Choosing an age shows its sessions or the configured fallback when dates are not posted.
- Private evaluations remain behind the page's private-evaluation notice rather than appearing as public dates.
- Session rows present the evaluation type, date, time, location, and registration action in a consistent table.

When hiding an age, update both the age-chart availability and any scheduled group for that age so the selector and sessions remain consistent.

## Update tryout schedule dates

Edit `data/tryouts.yaml` under `groups:`.

Example:

```yaml
- age_group: Rising 12U
  coach: Ken Torres
  sessions:
    - type: Open Evaluation
      date: Tuesday, May 5, 12, 19, 26
      time: 6:00–8:00 pm
      location: Dale City Recreation Center, Baseball Field 2
```

If a value includes a colon, quote it:

```yaml
coach: "Black: Chris Cheshire · Orange: Tim Jacoby"
```

## Update the age chart

Edit `age_chart.rows` in `data/tryouts.yaml`.

```yaml
age_chart:
  title: 2027 Baseball Age Chart
  rows:
    - age_group: 14U
      birth_window: May 1, 2012 – April 30, 2013
```

To retain an age definition without listing it for the current tryout cycle, set:

```yaml
- age_group: 11U
  enabled: false
  birth_window: May 1, 2015 – April 30, 2016
```

When an age is unavailable, also update the page intro and remove or comment out any active `groups` schedule block for that age. Remove `enabled` or change it to `true` when the age returns.

## Update FAQ

Edit the `faq:` list in `data/tryouts.yaml`.

```yaml
faq:
  - question: How do I register?
    answer: Use the Become a Tiger registration link on this page.
```

See [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md) for the full new-season and team-availability workflow.
