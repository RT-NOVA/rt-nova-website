# Coaching Opportunities Clean Hugo Refresh Patch

This reworks `/coaching-opportunities/` using the latest uploaded ZIP as the base.

## What changed

- Replaced the old-site style large split-feature sections.
- Removed orange side bars from value/support cards.
- Removed giant `HEAD` / `ASSIST` role art from the role cards.
- Changed the role cards into cleaner cards with smaller headings.
- Replaced the black-header comparison table with compact comparison rows.
- Replaced the responsibilities table with clean expectation rows.
- Changed the dark compensation/support band into light support cards.
- Kept the kicker / heading / note rhythm.
- Kept content/data in `data/coaching_opportunities.yaml`.
- Kept styling isolated to `assets/css/coaching-opportunities.css`.

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-coaching-opportunities-clean-hugo-refresh-patch.zip -d .

hugo server -D --disableFastRender
```

Then hard refresh:

```text
Cmd + Shift + R
```

## Verify

```bash
rg -n 'border-left|split-feature|coaching-support-section|coaching-role-card__short|coaching-table' layouts/partials/page-coaching-opportunities.html assets/css/coaching-opportunities.css
rg -n 'navy|#061120|#0c1b2e|#07101f|#07111f|#080f1b|#0f172a' assets/css/coaching-opportunities.css layouts/partials/page-coaching-opportunities.html
```

Expected: no output.
