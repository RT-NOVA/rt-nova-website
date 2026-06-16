# Roster Pages

Roster pages live under `content/rosters/` and are powered by Markdown front matter.

## Page structure

Individual roster pages use an open, Social Hub-inspired flow:

1. Hero
   - Kicker: `Roster`
   - Title: generated from `term`, for example `Spring 2026 Roster`
   - Intro: generated from `age_group` and `division`, for example `13U Black`
2. Small navigation row
   - Back to Team Central
   - All Rosters
3. Players card grid
4. Staff card grid

There is no large outer roster dashboard card around the full page. Player and staff cards sit directly on the page background to keep the page open and consistent with the homepage Social Hub style.

## Front matter fields

Required/recommended fields:

```yaml
title: "2026 13U Black Roster"
date: 2026-06-16
season: "2026 Season"
term: "Spring 2026"
age_group: "13U"
division: "Black"
record: "—"
summary: "Rawlings Tigers NOVA 13U Black spring roster and staff."
players:
  - number: "94"
    name: "Henry Bambling"
    positions: "P, 1B, 2B"
    image: "/images/rosters/2026-13u-black/henry-bambling.jpg"
staff:
  - name: "Chris Cheshire"
    title: "Head Coach"
    image: "/images/coaches/chris-cheshire.jpg"
```

## Player card display

Player cards display:

```text
Full Name #Number
Positions
```

If `image` is missing, an initial-based placeholder is shown.

## Staff card display

Staff cards display:

```text
Full Name
Title
```

If `image` is missing, an initial-based placeholder is shown.

## Image recommendations

For best results:

- Use consistent crop and framing across a roster.
- Prefer head/upper-body photos.
- Keep image aspect ratios close to 4:3.
- Store images in a predictable folder such as:

```text
static/images/rosters/2026-13u-black/
```

Then reference them as:

```yaml
image: "/images/rosters/2026-13u-black/player-name.jpg"
```

## Mobile behavior

The roster grid is responsive:

- Desktop: 4 cards per row
- Small desktop/tablet: 3 cards per row
- Tablet/large phone: 2 cards per row
- Phone: 1 card per row

Always test roster pages at approximately 390px, 430px, 768px, 1024px, and desktop widths before publishing major layout changes.
