# Watch Now page

`/watch-now/` is the current-team live media hub.

## Files

- `content/watch-now.md`
- `layouts/partials/page-watch-now.html`
- `assets/css/watch-now.css`
- `data/navigation.yaml`
- seasonal team files under `data/seasons/<season-id>/teams.yaml`

## Team source and visibility

The page selects the season marked `current` in `data/seasons/index.yaml`. It uses enabled Spring teams when populated, otherwise enabled Fall teams.

A team appears here only while it is enabled in the current season. This shares the same visibility filtering as Team Central and the Coaches page.

## GameChanger links

Add a team link with the exact `GameChanger` label:

```yaml
links:
  - label: GameChanger
    url: https://web.gc.com/teams/example/team
```

The Watch Now page normalizes a trailing `/team` segment and links to the main team page. Teams without a GameChanger URL display `Link coming soon`.

GameChanger may require a login, team membership, or viewing access. Keep that note on the page.

## Other media

An optional program-level YouTube streams URL can be set in the front matter for `content/watch-now.md`. GameChanger remains the primary current-team source.

Watch Now is linked from:

- the Teams navigation dropdown
- the desktop header camera shortcut
- the mobile navigation actions

If the route changes, update all three locations together and verify accessible labels for the icon-only shortcut.
