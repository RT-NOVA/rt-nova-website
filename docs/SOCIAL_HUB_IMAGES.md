# Social Hub Image Workflow

Facebook and Instagram post images should be stored locally in this repo.

Do not rely on direct Facebook or Instagram CDN image URLs such as `fbcdn.net`, `scontent.*`, or `cdninstagram.com` as the primary `image:` value. Those URLs often expire, block hotlinking, or fail when the site is served from GitHub Pages.

## Recommended post front matter

Use the original social post URL for the click-through link:

```yaml
platform: "Facebook"
link: "https://www.facebook.com/..."
button: "View on Facebook"
```

Use a local image for the card:

```yaml
image: "/images/social/2026-06-15-facebook-11u-team-photo.jpg"
image_alt: "Rawlings Tigers NOVA 11U team photo"
image_fit: "cover"
```

Optionally keep the original remote image URL for one-time syncing only:

```yaml
source_image_url: "https://scontent..."
```

## Sync utility

Run the utility from the repo root:

```bash
python3 scripts/social-hub-image-sync.py --dry-run
python3 scripts/social-hub-image-sync.py
```

The utility scans `content/social-hub/*.md`.

It will:

1. Use `source_image_url` when present.
2. Otherwise use a remote `image: https://...` value as the source.
3. Download the image into `static/images/social/`.
4. Update the post to use the local `/images/social/...` path.
5. Preserve the remote URL as `source_image_url`.

## If download fails

Facebook and Instagram CDN URLs can expire. When that happens:

1. Open the original post from the `link:` field.
2. Save the correct image manually.
3. Put it in `static/images/social/`.
4. Update the post front matter:

```yaml
image: "/images/social/the-saved-image.jpg"
image_fit: "cover"
```

## New Social Hub content checklist

For every new Facebook or Instagram card:

- Keep `link:` pointed to the real post.
- Use a local `image:` path under `/images/social/`.
- Write useful `image_alt:`.
- Use `image_fit: "cover"` for normal photo cards.
- Use `image_fit: "contain"` for graphics/posters that should not crop.
- Avoid direct CDN URLs as the final `image:` value.
