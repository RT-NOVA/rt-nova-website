# Homepage Photo Controls

The homepage uses photos inside existing sections rather than adding a separate photo gallery section.

## Hero image

The homepage hero image is controlled in `data/homepage.yaml`:

```yaml
hero:
  image: /images/program-media/homepage-team-hero.png
  image_position: center 42%
```

To rotate the hero image:

1. Add the new image under `static/images/program-media/` or another `static/images/...` folder.
2. Update `hero.image` to the new path.
3. Adjust `hero.image_position` if the crop needs to focus higher/lower or left/right.

Useful examples:

```yaml
image_position: center center
image_position: center 35%
image_position: 60% center
image_position: left center
```

Recommended hero images should be wide landscape images. A good target is roughly 1600×900 or wider.

## Built Around Growth section image

The image in the “Built around growth, competition, and love for the game” section is controlled by the `why.image` block:

```yaml
why:
  image:
    enabled: true
    src: /images/social/2026-06-15-facebook-11u-team-facebook-photo.jpg
    alt: Rawlings Tigers NOVA players together after a team moment.
    position: center center
    label: NOVA Baseball Family
    caption: Real players, real teams, and a program built around the day-to-day experience.
```

To hide the image and return that section to the centered text-only layout:

```yaml
enabled: false
```

Use candid team, practice, dugout, or game-day photos here. This section works best with a warm, personal team image rather than a graphic or player-card image.
