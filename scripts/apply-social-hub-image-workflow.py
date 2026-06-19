#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
css_path = ROOT / "assets" / "css" / "social-hub.css"
readme_path = ROOT / "docs" / "SOCIAL_HUB_README.md"
images_doc_path = ROOT / "docs" / "SOCIAL_HUB_IMAGES.md"

if not css_path.exists():
    raise SystemExit("Missing assets/css/social-hub.css. Run from the repo root.")

# Keep Social Hub placeholders on the new black/charcoal/orange system.
css = css_path.read_text()
css = css.replace("rgba(8,15,27,.08)", "rgba(5,5,5,.08)")
css = css.replace("rgba(8, 15, 27, .08)", "rgba(5,5,5,.08)")
css = css.replace("linear-gradient(135deg,var(--rt-navy),#0f172a)", "linear-gradient(135deg,#050505,#151515)")

marker = "/* Social Hub local image workflow */"
if marker not in css:
    css = css.rstrip() + """

/* Social Hub local image workflow */
.social-feed-card__image--placeholder {
  background:
    radial-gradient(circle at 20% 20%, rgba(245,91,32,.14), transparent 32%),
    linear-gradient(135deg,#050505,#151515);
}

.social-feed-card__image--placeholder span {
  color:rgba(255,255,255,.9);
}
"""
css_path.write_text(css)
print(f"Updated {css_path}")

# Add/update dedicated image workflow docs.
images_doc_path.parent.mkdir(exist_ok=True)
images_doc_path.write_text("""# Social Hub Image Workflow

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
""")
print(f"Wrote {images_doc_path}")

# Add a short pointer into existing Social Hub README if present.
if readme_path.exists():
    readme = readme_path.read_text()
    pointer = """\n## Social Hub images\n\nFor Facebook and Instagram cards, use local images under `static/images/social/` instead of direct CDN hotlinks. See `docs/SOCIAL_HUB_IMAGES.md` and run:\n\n```bash\npython3 scripts/social-hub-image-sync.py --dry-run\npython3 scripts/social-hub-image-sync.py\n```\n"""
    if "SOCIAL_HUB_IMAGES.md" not in readme:
        readme = readme.rstrip() + "\n" + pointer
        readme_path.write_text(readme)
        print(f"Updated {readme_path}")
    else:
        print(f"{readme_path} already references SOCIAL_HUB_IMAGES.md")
else:
    print(f"Skipped missing {readme_path}")

# Audit changed text files for old navy values.
bad_patterns = [
    "#061120", "#0c1b2e", "#07101f", "#07111f", "#080f1b", "#0f172a",
    "rgba(6,17,32", "rgba(6, 17, 32",
    "rgba(3,10,20", "rgba(3, 10, 20",
    "rgba(8,15,27", "rgba(8, 15, 27",
    "rgba(7,16,31", "rgba(7, 16, 31",
    "navy",
]
hits = []
for path in [css_path, images_doc_path, readme_path]:
    if not path.exists():
        continue
    body = path.read_text(errors="ignore")
    for i, line in enumerate(body.splitlines(), start=1):
        low = line.lower()
        if any(pattern.lower() in low for pattern in bad_patterns):
            hits.append(f"{path}:{i}: {line.strip()}")

if hits:
    print("\\nWARNING: possible old navy references found:")
    for hit in hits:
        print(hit)
    raise SystemExit(2)

print("Verified: changed Social Hub workflow files did not introduce old navy values.")
print("Next: run python3 scripts/social-hub-image-sync.py --dry-run")
