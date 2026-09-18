# Tryouts Page Maintenance

The Tryouts page is rendered from:

```text
data/tryouts.yaml
layouts/partials/page-tryouts.html
assets/css/tryouts.css
assets/js/tryouts.js
```

## Current page behavior

The age chart is expanded on page load. Its disclosure control says “Hide Chart” while expanded and “Show Chart” while collapsed.

The page combines the published age chart and scheduled `groups` into one age-group selector:

- The all-ages view shows only real published evaluation sessions.
- Choosing an age shows its sessions or the configured fallback when dates are not posted.
- Private evaluations remain behind the page's private-evaluation notice rather than appearing as public dates.
- Session rows present the evaluation type, date, time, location, and map link in a consistent table. Groups with posted sessions have one registration button below the table.

When hiding an age, update both the age-chart availability and any scheduled group for that age so the selector and sessions remain consistent.

## Update tryout schedule dates

Edit `data/tryouts.yaml` under `groups:`.

Example:

```yaml
- age_group: 12U
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

## Set the location and map link

Each session supports two location fields:

- `location`: the text displayed in the schedule. Include the city/state or full address when needed to identify the correct park or field.
- `directions_url` (optional): the exact URL opened by the map icon. Use a verified map or directions link for the correct venue, entrance, or field.

For example:

```yaml
sessions:
  - type: Open Evaluations
    date: 09/23/2026
    time: 6:00 PM
    location: Cloverdale Park, Dale City, VA
    directions_url: "https://www.google.com/maps/search/?api=1&query=Cloverdale+Park+Dale+City+VA"
```

The example uses a Google Maps search URL; you can replace it with the share link copied from the verified venue in Google Maps.

The page uses `directions_url` when supplied. If it is omitted or blank, the page creates a Google Maps search URL using the `location` text exactly as entered; it does not automatically add a city or state. If neither a map URL nor a usable location is supplied (the location is missing, blank, or `—`), the Map column shows `—` instead of a link.

Set these fields separately for each session when dates use different venues.

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

## Registration links

`registration_url` in `data/tryouts.yaml` points to `/become-a-tiger/`. Keep it a plain page path without a query string: group registration buttons append `?age=<age_group>`.

A group with posted sessions displays `REGISTER FOR <age_group>`. For example, `11U` links to `/become-a-tiger/?age=11U`, which preselects that age in the embedded Jotform. Use the exact age values `10U`, `11U`, `12U`, `13U`, or `14U`; labels such as `Rising 12U` do not match the registration script's allowlist.

The orange global private-tryout notice has a **Request a Tryout** link to the same registration page without an age parameter. The page's final **Become a Tiger** link also leaves age selection to the visitor. Registration records interest in an age group; it does not select or reserve a particular evaluation date.

See [`PLAYER_REGISTRATION_README.md`](PLAYER_REGISTRATION_README.md) for the Jotform field mapping and verification steps. When promoting an evaluation through the global announcement bar, maintain its message separately in `data/announcement.yaml` and disable or update it after the event; see [`ANNOUNCEMENT_BAR_README.md`](ANNOUNCEMENT_BAR_README.md).

## Update FAQ

Edit the `faq:` list in `data/tryouts.yaml`.

```yaml
faq:
  - question: How do I register?
    answer: Use the Become a Tiger registration link on this page.
```

See [`SEASON_MAINTENANCE.md`](SEASON_MAINTENANCE.md) for the full new-season and team-availability workflow.
