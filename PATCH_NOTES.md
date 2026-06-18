# Tryout Schedule Clean Session + Directions Patch

This replaces the boxed/badge treatment for `Open Evaluation` and `Formal Tryout` with a cleaner text label and small dot.

It also adds a clickable directions icon for each schedule row.

## Visual behavior

- Open Evaluation: orange dot + orange text
- Formal Tryout: navy dot + navy text
- Directions: compact map icon on the far right of the row

## Directions behavior

The directions icon opens Google Maps using the session location.

If a session ever needs a custom map link, add this optional field to that session in `data/tryouts.yaml`:

```yaml
directions_url: "https://www.google.com/maps/search/?api=1&query=Veterans%20Memorial%20Park%20Baseball%20Field%204"
```

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-tryout-clean-sessions-directions-patch.zip -d .

python3 scripts/apply-tryout-clean-sessions-directions.py

hugo server -D --disableFastRender
```

## Files modified by script

- `layouts/partials/page-tryouts.html`
- `assets/css/tryouts.css`
