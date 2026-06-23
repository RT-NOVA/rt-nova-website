# Homepage Media

The homepage keeps photos integrated into existing sections instead of adding a separate gallery-style block.

## Hero image

The homepage hero image is controlled in `data/homepage.yaml`:

```yaml
hero:
  image: /images/program-media/13u-coach-talk.jpg
  image_position: center 55%
```

Use `image_position` to adjust the crop/focus without editing CSS. Examples:

```yaml
image_position: center center
image_position: center 35%
image_position: right center
```

This maps to CSS `object-position`, so it changes which part of the image stays visible when the hero crops across desktop, tablet, and mobile screens.

## Built Around Growth image

The optional photo inside the `Built around growth, competition, and love for the game` section is controlled by:

```yaml
why:
  image:
    enabled: true
    src: /images/program-media/main-love-the-game-1600x1200-crop.jpg
    alt: Rawlings Tigers NOVA players together after a team moment.
    position: center center
```

Set `enabled: false` to return the section to text-only.

Recommended image sizes:

- Hero: 2000–2400px wide, landscape.
- Built Around Growth: 1600 × 1200, 1800 × 1200, or similar landscape crop.

## Local/training teaser

The homepage also includes a small local/training footprint teaser inside the Built Around Growth section:

```yaml
why:
  local:
    enabled: true
    callouts:
      - title: Local roots
        text: Serving Woodbridge, Dumfries, Montclair, Dale City, Stafford, Manassas, Fairfax, Prince William County, and surrounding communities.
      - title: Real training locations
        text: Outdoor work centers on Woodbridge-area fields, with winter training at D-BAT Manassas, Metro Baseball Facility, and Veterans Community Center.
    link:
      label: View Training Locations
      url: /training-locations/
```

Keep these callouts short so the homepage remains a teaser and the Training Locations page remains the detailed planning page.
