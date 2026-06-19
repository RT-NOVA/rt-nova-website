#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
css_path = ROOT / "assets" / "css" / "social-hub.css"
partial_path = ROOT / "layouts" / "partials" / "social-hub-card.html"
instagram_post = ROOT / "content" / "social-hub" / "2026-instagram-direct-image-test.md"

if not css_path.exists():
    raise SystemExit("Missing assets/css/social-hub.css. Run from the repo root.")
if not partial_path.exists():
    raise SystemExit("Missing layouts/partials/social-hub-card.html. Run from the repo root.")

# 1) Make the Instagram flyer/poster use contain so it does not crop.
if instagram_post.exists():
    text = instagram_post.read_text()
    if 'image_fit: "cover"' in text:
        text = text.replace('image_fit: "cover"', 'image_fit: "contain"', 1)
        instagram_post.write_text(text)
        print(f"Updated {instagram_post}: image_fit cover -> contain")
    else:
        print(f"{instagram_post}: no image_fit cover value to update")
else:
    print(f"Skipped missing {instagram_post}")

# 2) Ensure the Social Hub card partial gives the media wrapper a fit class.
partial = partial_path.read_text()

if "social-feed-card__image--{{ $imageFit }}" not in partial:
    partial, count = re.subn(
        r'<div class="social-feed-card__image">',
        r'<div class="social-feed-card__image social-feed-card__image--{{ $imageFit }}">',
        partial,
        count=1,
    )

    if count == 0:
        partial, count = re.subn(
            r'<div class="([^"]*\bsocial-feed-card__image\b[^"]*)">',
            r'<div class="\1 social-feed-card__image--{{ $imageFit }}">',
            partial,
            count=1,
        )

    if count == 0:
        raise SystemExit("Could not find social-feed-card__image wrapper in social-hub-card.html.")

    partial_path.write_text(partial)
    print(f"Updated {partial_path}: added image-fit class to media wrapper")
else:
    print(f"{partial_path}: image-fit class already present")

# 3) Add/replace CSS rules so cover and contain behave correctly.
css = css_path.read_text()

start = "/* Social Hub image fit fix */"
end = "/* End Social Hub image fit fix */"
css = re.sub(rf"\n?{re.escape(start)}[\s\S]*?{re.escape(end)}\n?", "\n", css)

fit_css = """
/* Social Hub image fit fix */
.social-feed-card__image {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #f5f5f5;
  border-top: 1px solid rgba(5,5,5,.12);
  border-bottom: 1px solid rgba(5,5,5,.12);
  overflow: hidden;
}

.social-feed-card__image img {
  display: block;
  width: 100%;
  height: 100%;
  object-position: center center;
}

.social-feed-card__image--cover img {
  object-fit: cover;
}

.social-feed-card__image--contain {
  background:
    radial-gradient(circle at 18% 20%, rgba(245,91,32,.08), transparent 34%),
    #f7f7f7;
}

.social-feed-card__image--contain img {
  object-fit: contain;
  padding: .75rem;
}

@media (max-width: 720px) {
  .social-feed-card__image {
    aspect-ratio: 4 / 3;
  }

  .social-feed-card__image--contain img {
    padding: .55rem;
  }
}
/* End Social Hub image fit fix */
"""

css = css.rstrip() + "\n\n" + fit_css.strip() + "\n"
css_path.write_text(css)
print(f"Updated {css_path}: added stable cover/contain image rules")

# 4) Verify no old navy values are introduced.
bad_patterns = [
    "#061120", "#0c1b2e", "#07101f", "#07111f", "#080f1b", "#0f172a",
    "rgba(6,17,32", "rgba(6, 17, 32",
    "rgba(3,10,20", "rgba(3, 10, 20",
    "rgba(8,15,27", "rgba(8, 15, 27",
    "rgba(7,16,31", "rgba(7, 16, 31",
    "navy",
]
hits = []
for path in [css_path, partial_path, instagram_post]:
    if not path.exists():
        continue
    body = path.read_text(errors="ignore")
    for i, line in enumerate(body.splitlines(), start=1):
        low = line.lower()
        if any(pattern.lower() in low for pattern in bad_patterns):
            hits.append(f"{path}:{i}: {line.strip()}")

if hits:
    print("\nWARNING: possible old navy references found:")
    for hit in hits:
        print(hit)
    raise SystemExit(2)

print("Verified: changed Social Hub image-fit files did not introduce old navy values.")
print("Run: hugo server -D --disableFastRender")
