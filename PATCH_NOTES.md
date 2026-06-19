# RT NOVA Navy Cleanup Final Pass

This patch does a broader cleanup than the first theme patch.

## What it does

- Scans active CSS files in `assets/css/*.css`.
- Converts the main dark variables:
  - `--rt-navy` to `#0b0b0d`
  - `--rt-navy-2` to `#151515`
- Replaces common hard-coded navy/slate colors and blue-tinted rgba shadows/overlays in served CSS files.
- Adds stronger global overrides for:
  - page heroes
  - homepage hero overlay
  - header
  - footer
  - dark sections
  - Booster Club contact/CTA sections
  - Sponsorship contact/CTA sections
  - table headers
  - Social Hub dark placeholders/buttons
- Writes `NAVY_CLEANUP_AUDIT.md` with any remaining hard-coded old navy/blue values.

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-navy-cleanup-audit-patch.zip -d .

python3 scripts/apply-navy-cleanup-final-pass.py

hugo server -D --disableFastRender
```

Then hard refresh:

```text
Cmd + Shift + R
```

## Verify

```bash
rg -n "#061120|#0c1b2e|#07101f|#07111f|#080f1b|#0f172a|rgba\(6,\s*17,\s*32|rgba\(3,\s*10,\s*20|rgba\(8,\s*15,\s*27|rgba\(7,\s*16,\s*31" assets/css --glob "*.css"
```

It is okay if `var(--rt-navy)` still appears. The variable now points to near-black.
