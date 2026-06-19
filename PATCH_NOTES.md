# Coaching Opportunities Cleanup v3 Patch

This patch makes the latest requested cleanup to `/coaching-opportunities/`.

## Changes

- Removes all hero buttons from the Coaching Opportunities hero:
  - Apply Now
  - Head Coach PDF
  - Assistant Coach PDF
- Removes the Start and Type/Paid Position sub-cards from Head Coach and Assistant Coach cards.
- Removes Apply Now from the Head Coach and Assistant Coach cards.
- Keeps the PDF download buttons on the role cards.
- Removes the duplicate `Job Description Downloads / Download the role listings` section.
- Keeps the white proof-strip text consistent, so `Compensation` and `Paid Positions` use the same neutral dark color as the other quick facts.
- Differentiates role callouts:
  - Head / Lead Role = orange treatment
  - Assistant / Support Role = black/charcoal treatment
- Differentiates Applies To pills:
  - Head = orange
  - Assistant = black/charcoal
  - Both = cream/neutral

## Navy verification

The apply script checks the modified coaching files and fails if it introduces old navy values or the word `navy`.

## Apply

```bash
cd /Users/smbambling/Documents/personal/git/github/rt-nova-website

unzip -o ~/Desktop/rt-nova-coaching-cleanup-v3-patch.zip -d .

python3 scripts/apply-coaching-cleanup-v3.py

hugo server -D --disableFastRender
```

Then hard refresh:

```text
Cmd + Shift + R
```

## Files modified by script

- `layouts/partials/page-coaching-opportunities.html`
- `assets/css/coaching-opportunities.css`
