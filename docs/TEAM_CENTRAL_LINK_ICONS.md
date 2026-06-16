# Team Central Link Icons

Team Central uses icon-only links for each team row.

## Link labels

The renderer recognizes these labels in `data/teams.yaml`:

- `Facebook`
- `Instagram`
- `Roster`
- `Schedule`
- `GameChanger`
- `Accolades`

## Current icon behavior

- `Roster` uses the legacy two-person roster SVG and is highlighted orange.
- `Schedule` uses the legacy calendar SVG.
- `GameChanger` renders as a `GC` text badge.
- `Accolades` uses the legacy trophy SVG.
- `Accolades` is currently a placeholder with `url: ""` and `placeholder: true` until team-specific accolades exist.

## Roster links

Roster links should point to the new Hugo roster pages, for example:

```yaml
- label: "Roster"
  url: "/rosters/2026-13u-black/"
```

## Accolades placeholder

Until the new accolades anchors exist, keep:

```yaml
- label: "Accolades"
  url: ""
  placeholder: true
```

When team-specific accolade anchors are ready, update to something like:

```yaml
- label: "Accolades"
  url: "/accolades/#team-2026-13u-black"
```

and remove `placeholder: true`.
