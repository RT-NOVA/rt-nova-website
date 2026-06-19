#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
social_dir = ROOT / "content" / "social-hub"
partial_path = ROOT / "layouts" / "partials" / "social-hub-card.html"

if not social_dir.exists():
    raise SystemExit("Missing content/social-hub directory. Run from the repo root.")
if not partial_path.exists():
    raise SystemExit("Missing layouts/partials/social-hub-card.html. Run from the repo root.")

replacements = [
    {
        "file": social_dir / "2026-facebook-11u-photo-example.md",
        "local_image": "/images/social/11u-black-champions.jpeg",
        "fit": "cover",
    },
    {
        "file": social_dir / "2026-instagram-direct-image-test.md",
        "local_image": "/images/social/instagram-team-moments.svg",
        "fit": "cover",
    },
]

for item in replacements:
    path = item["file"]
    if not path.exists():
        print(f"Skipped missing {path}")
        continue

    text = path.read_text()

    image_match = re.search(r'^image:\s*"?(https?://[^"\n]+)"?\s*$', text, flags=re.MULTILINE)
    if image_match and "source_image_url:" not in text:
        source = image_match.group(1)
        text = text.replace(
            image_match.group(0),
            f'source_image_url: "{source}"\nimage: "{item["local_image"]}"',
            1,
        )
    else:
        text = re.sub(
            r'^image:\s*".*?"\s*$',
            f'image: "{item["local_image"]}"',
            text,
            count=1,
            flags=re.MULTILINE,
        )

    image_alt_match = re.search(r'^image_alt:.*$', text, flags=re.MULTILINE)
    if "image_fit:" in text:
        text = re.sub(r'^image_fit:\s*".*?"\s*$', f'image_fit: "{item["fit"]}"', text, count=1, flags=re.MULTILINE)
    elif image_alt_match:
        text = text.replace(image_alt_match.group(0), image_alt_match.group(0) + f'\nimage_fit: "{item["fit"]}"', 1)

    path.write_text(text)
    print(f"Updated {path} to use stable local image {item['local_image']}")

partial = partial_path.read_text()

old_block = """{{ $image := $post.Params.image }}
{{ $imageFit := $post.Params.image_fit | default "contain" }}
{{ $imgSrc := "" }}
{{ $imgExternal := false }}
{{ with $image }}
  {{ $imgSrc = . }}
  {{ if or (hasPrefix . "http://") (hasPrefix . "https://") }}
    {{ $imgExternal = true }}
  {{ else }}
    {{ $imgSrc = partial "url.html" . }}
  {{ end }}
{{ end }}"""

new_block = """{{ $image := $post.Params.image }}
{{ $imageFit := $post.Params.image_fit | default "contain" }}
{{ $fallbackImage := $post.Params.fallback_image | default "" }}
{{ $imgSrc := "" }}
{{ $imgExternal := false }}
{{ with $image }}
  {{ $imgSrc = . }}
  {{ if or (hasPrefix . "http://") (hasPrefix . "https://") }}
    {{ $imgExternal = true }}
    {{ $lowerImg := lower . }}
    {{ if or (in $lowerImg "fbcdn.net") (in $lowerImg "cdninstagram.com") }}
      {{ if ne $fallbackImage "" }}
        {{ $imgSrc = partial "url.html" $fallbackImage }}
      {{ else if eq $sourceType "facebook" }}
        {{ $imgSrc = partial "url.html" "/images/social/facebook-program-update.svg" }}
      {{ else if eq $sourceType "instagram" }}
        {{ $imgSrc = partial "url.html" "/images/social/instagram-team-moments.svg" }}
      {{ end }}
      {{ $imgExternal = false }}
    {{ end }}
  {{ else }}
    {{ $imgSrc = partial "url.html" . }}
  {{ end }}
{{ end }}"""

if old_block in partial:
    partial = partial.replace(old_block, new_block, 1)
else:
    print("Partial image block did not match exactly; checking if fallback logic already exists.")
    if "fbcdn.net" not in partial and "cdninstagram.com" not in partial:
        raise SystemExit("Could not patch layouts/partials/social-hub-card.html image handling safely.")

partial_path.write_text(partial)
print(f"Updated {partial_path} with Facebook/Instagram CDN fallback logic.")

for svg_path in [
    ROOT / "static/images/social/facebook-program-update.svg",
    ROOT / "static/images/social/instagram-team-moments.svg",
    ROOT / "static/images/social/static-program-note.svg",
]:
    if not svg_path.exists():
        continue
    svg = svg_path.read_text()
    svg = svg.replace("#07111f", "#0b0b0d").replace("#07101f", "#0b0b0d").replace("#061120", "#0b0b0d")
    svg = svg.replace("Orange and navy", "Orange and black")
    svg_path.write_text(svg)
    print(f"Updated {svg_path} placeholder colors to black/charcoal.")

docs = ROOT / "docs"
docs.mkdir(exist_ok=True)
doc_path = docs / "SOCIAL_HUB_IMAGES.md"
doc_path.write_text("""# Social Hub Images

Do not use direct Facebook CDN or Instagram CDN image URLs in `content/social-hub/*.md` as the primary `image` value.

Those URLs are temporary and often expire, block hotlinking, or break when served from GitHub Pages.

## Recommended pattern

Download or create a stable local image under:

```text
static/images/social/
```

Then reference it from the post front matter:

```yaml
image: "/images/social/my-social-image.jpg"
image_alt: "Short descriptive alt text"
image_fit: "cover"
```

Keep the Facebook or Instagram post URL in `link:` so visitors can click through to the original post:

```yaml
link: "https://www.facebook.com/..."
button: "View on Facebook"
```

## Optional fallback

If you need to preserve the original CDN image for reference, use:

```yaml
source_image_url: "https://scontent..."
image: "/images/social/local-fallback.jpg"
```

The Social Hub card partial also includes a defensive fallback: if a future card uses an `fbcdn.net` or `cdninstagram.com` image URL, it will render a local platform placeholder instead of showing a broken image icon.
""")
print(f"Wrote {doc_path}")

bad_patterns = [
    "#061120", "#0c1b2e", "#07101f", "#07111f", "#080f1b", "#0f172a",
    "rgba(6,17,32", "rgba(6, 17, 32",
    "rgba(3,10,20", "rgba(3, 10, 20",
    "rgba(8,15,27", "rgba(8, 15, 27",
    "rgba(7,16,31", "rgba(7, 16, 31",
    "navy",
]
check_files = [
    partial_path,
    social_dir / "2026-facebook-11u-photo-example.md",
    social_dir / "2026-instagram-direct-image-test.md",
    ROOT / "static/images/social/facebook-program-update.svg",
    ROOT / "static/images/social/instagram-team-moments.svg",
    ROOT / "static/images/social/static-program-note.svg",
    doc_path,
]
hits = []
for path in check_files:
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

print("Verified: no old navy hex/rgba values or 'navy' text were introduced in changed Social Hub text/SVG files.")
print("Run: hugo server -D --disableFastRender")
