# Heading System Cleanup

This patch normalizes heading size and font behavior across the site while preserving the existing page layouts.

## What stays the same

- Split/side-heading sections, such as About page overview blocks, remain side-by-side.
- Centered section headings remain centered.
- Data/list headings, such as team schedule groups and tryout age groups, remain compact.
- Page heroes are not redesigned.

## Shared heading tiers

### Major section headings

Used by `.rt-section-heading h2` and side/split sections via `.split-feature > div:first-child h2`.

### Compact block headings

Used by staff, accolade, coaching-opportunity, and similar internal content blocks.

### Data/list headings

Used by schedule team names, tryout age groups, and other table/list group headers.

## Files touched

- `assets/css/main.css`
- `assets/css/tryouts.css`
- `assets/css/coaches.css`
- `assets/css/coaching-opportunities.css`
- `assets/css/accolades.css`
- `assets/css/watch-now.css`
- `assets/css/team-central.css`
- `assets/css/schedules.css`

## v2 page-level section heading promotion

Promotes page-level section headers such as `/coaches/` `Program Leadership`, `Team Coaching Staff`, and `Coaching Standards` to the same major section heading tier used on `/tryouts/`, while preserving the existing page layout.

The key adjustment is that layout style and heading tier are now separate:

- Side/split headings may stay side-aligned.
- Centered headings may stay centered.
- Page-level section `h2` headings use the major section size/font.
- Internal card/subsection headings remain compact.

## v3 Accolades heading promotion

Promotes `/accolades/` page-level section headings such as `Banner Wall`, `Tournament Results`, and `Player Honors` to the same major section heading tier used on `/tryouts/` and `/coaches/`.

Accolades team/result cards remain data/list headings, but now use the shared data heading tier instead of their own smaller page-specific sizing.

## v4 final audit

Final pass for custom page-level headings that do not use the shared `.rt-section-heading` markup.

Additional coverage:

- Become a Tiger readiness/confirmation headings
- Roster page and roster section headings
- Team Central intro, season, and term headings
- Training Locations split/CTA headings
- Social Hub custom intro heading
- News index and related-section headings
- Final Tryouts guard against older accumulated heading overrides

This pass keeps layout intact and only aligns heading tiers.
