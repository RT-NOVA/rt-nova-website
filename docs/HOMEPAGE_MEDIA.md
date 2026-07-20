# Homepage media

Homepage copy and media are primarily configured in `data/homepage.yaml`. Images are normally stored under `static/images/program-media/` or `static/images/social/` and referenced with site-root paths such as `/images/program-media/example.jpg`.

## Hero slides

The homepage hero uses `hero.slides`:

```yaml
hero:
  interval: 4000
  transition_duration: 1600
  slides:
    - image: /images/program-media/cheshire-and-12u-black.jpeg
      image_position: center 30%
      mobile_position: center 30%
```

- Add another item to include it in the crossfade rotation.
- `interval` and `transition_duration` are milliseconds.
- `image_position` controls the desktop focal point.
- `mobile_position` provides a separate phone crop.
- Use natural images; do not add filters or shading unless the design direction is intentionally changing.

## Program Focus images

Each item under `pillars` owns its image, crop, destination, and accessible link label:

```yaml
- title: Professional Coaching
  image: /images/program-media/13u-coach-talk.jpg
  image_position: 85% center
  url: /coaches/
  link_label: Meet the Coaches
```

Use `image_position` to keep the important subject visible at different card widths. An optional `image_zoom` can be used for an asset that contains too much surrounding space, but the preferred solution is a suitable source image and focal position. Avoid zoom values that cut off players or coaching context.

## Player pathway and competitive-team image

The pathway stages and the recruiting copy are also in `data/homepage.yaml` under `pathway` and `recruiting`.

The competitive-team image is selected from current featured accolades when they are available. Featured achievement candidates come from season tournament-result data and rotate on the homepage. See [`ACCOLADES_README.md`](ACCOLADES_README.md) for the fields that control the image, link, crop, and featured status.

If no featured achievement is available, the homepage falls back to:

```yaml
recruiting:
  image: /images/social/black-13u-sweep-championship-victory.jpeg
  image_alt: Rawlings Tigers NOVA 13U Black players with their championship banner and medals.
```

Keep the fallback image and alt text current even when featured achievements normally supply the visible image.

## Local Roots image

The Local Roots section has an optional image block:

```yaml
why:
  image:
    enabled: false
    src: /images/program-media/main-love-the-game-1600x1200-crop.jpg
    alt: Rawlings Tigers NOVA players together after a team moment.
    position: center center
```

Leave `enabled: false` for the approved centered text-and-callout layout. Enable it only as an intentional section redesign.

## Image checklist

- Use descriptive `alt` text that explains the actual team or moment.
- Prefer large originals; roughly 2000px wide is appropriate for hero images.
- Check desktop, tablet, and phone crops after changing an image.
- Verify that linked images show a pointer cursor and a visible keyboard focus state.
- Do not edit the generated copies in `public/`.
