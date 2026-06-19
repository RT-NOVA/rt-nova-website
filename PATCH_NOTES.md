# Social Hub Image Fit Fix Patch

This patch fixes downloaded Social Hub images not sitting correctly inside their cards.

## What it changes

- Makes the Social Hub image wrapper use a stable 4:3 media area.
- Ensures `image_fit: "cover"` fills the card cleanly.
- Ensures `image_fit: "contain"` shows the whole image without cropping.
- Sets the Instagram flyer/poster card to `image_fit: "contain"` so the full graphic is visible.
- Keeps the Facebook team photo as `cover`, which is better for normal photo cards.
- Verifies the changed files do not reintroduce the old navy values.

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-social-hub-image-fit-fix-patch.zip -d .

python3 scripts/apply-social-hub-image-fit-fix.py

hugo server -D --disableFastRender
```

Then hard refresh:

```text
Cmd + Shift + R
```

## How to choose image_fit

Use this in Social Hub front matter:

```yaml
image_fit: "cover"
```

for normal photos that can crop slightly.

Use:

```yaml
image_fit: "contain"
```

for flyers, posters, graphics, sponsor images, or anything where text/logos should not crop.
