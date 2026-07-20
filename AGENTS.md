# Rawlings Tigers NOVA website

This repository contains the Hugo website for Rawlings Tigers NOVA. The current working tree is the source of truth.

## Before changing the site

1. Read [`docs/README.md`](docs/README.md).
2. Read the guide for the page or data being changed.
3. Run `git status --short` and preserve unrelated work.
4. Inspect the current implementation and rendered page before editing.
5. Make the smallest component-scoped change that satisfies the request.

Do not reset, clean, restore, pull, switch branches, or replace files with an older patch unless the user explicitly requests it. Do not edit generated files under `public/`.

## Source and generated content

- Team, roster, schedule, tryout, coach, accolade, and season workflows are indexed in `docs/README.md`.
- Roster source data lives under `data/seasons/<season-id>/rosters/`. Do not edit generated roster pages in `content/rosters/` directly.
- Team visibility is controlled independently in the team and roster data; follow `docs/SEASON_MAINTENANCE.md`.
- Front-end ownership and the responsive test matrix are documented in `docs/FRONTEND_MAINTENANCE.md`.

## Change discipline

- Do not rewrite an entire CSS file to change one component.
- Prefer the original owning selector over a new override.
- Avoid broad selectors such as `main > :first-child` and `section:first-child`.
- Do not modify the homepage, header, footer, Social Hub, or unrelated pages while fixing another component.
- Use the actual component classes when correcting hero or responsive behavior.
- Treat `assets/css/design-lock.css` as a preservation layer, not a routine editing target.
- Explain the root cause before making a visual fix and verify the rendered result afterward.

## Hugo and validation

Local and Cloudflare builds use Hugo Extended `0.164.0`.

For content/data changes, run:

```bash
python3 scripts/sync-roster-pages.py --check
```

For all changes, run:

```bash
hugo --minify --cleanDestinationDir
bash scripts/validate-local-assets.sh
bash scripts/validate-site.sh public
```

For visual changes, also review the affected routes at wide desktop, medium desktop, tablet, and mobile widths. Check initial and scrolled header states where applicable.
