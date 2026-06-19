# Coaches Heading + Bio Cleanup Patch

## What changed

- Keeps the current staff row/table flow.
- Centers the section heading blocks on desktop/tablet.
- Keeps the kicker / heading / note feel.
- Keeps section heading size below hero scale so it better matches the other pages.
- Replaces the boxed `Bio +` badge with a subtle inline text action.
- Keeps `Bio +` wording, changing to `Bio −` when expanded.
- Leaves the photo preview behavior unchanged.

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-coaches-heading-bio-cleanup-patch.zip -d .

hugo server -D --disableFastRender
```

Then hard refresh:

```text
Cmd + Shift + R
```

## Verify

```bash
rg -n 'rt-coaches-bio-toggle|rt-coaches-block-head' assets/css/coaches.css
rg -n 'navy|#061120|#0c1b2e|#07101f|#07111f|#080f1b|#0f172a' assets/css/coaches.css
```
