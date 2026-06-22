# Watch Now Page

Reworks `/watch-now/` into a current-team live media hub.

## Content source

The older legacy site page positioned Watch Now as a place for live games, highlights, team updates, archived video, and streaming content through GameChanger and program media sources.

## Behavior

- Shows current teams only.
- Current teams are determined from `data/seasons/index.yaml` and `data/seasons/<season-id>/teams.yaml`.
- Uses each team's `GameChanger` link when present.
- Does not show Facebook or Instagram links.
- Teams without GameChanger links show `Link coming soon`.
- Adds Watch Now under the Teams dropdown in `data/navigation.yaml`.

## Files

- `content/watch-now.md`
- `layouts/partials/page-watch-now.html`
- `assets/css/watch-now.css`
- `layouts/_default/single.html`
- `data/navigation.yaml`

## v2 GameChanger URL cleanup

Watch Now normalizes team GameChanger links by removing a trailing `/team` path segment so buttons open the main team page instead of the roster/team subpage.

## v3 header shortcut

- Ensures `Watch Now` is listed under the Teams dropdown in `data/navigation.yaml`.
- Adds a small Watch Now video icon shortcut to the desktop header actions.
- Adds a prominent Watch Now shortcut to the mobile menu actions.

## v4 camera icon

Changed the Watch Now header shortcut from the YouTube-style icon to a camera/video icon so it represents live video without looking like a YouTube-specific link.
