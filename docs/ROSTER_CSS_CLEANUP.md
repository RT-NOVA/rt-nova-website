# Roster CSS cleanup

This update replaces the accumulated roster CSS overrides with one clean `assets/css/rosters.css` file.

## Intended roster card behavior

- Player cards use a light media area when no image is set.
- Missing images show a centered, solid black circle with a white first initial.
- No silhouette SVG is required.
- No orange ring, outline, or extra placeholder image is used.
- Player names are dark and bold.
- Player numbers are orange, larger, and aligned to the right.
- Cards remain responsive: 4 columns desktop, 3 tablet, 2 small tablet, 1 phone.

## Cleanup script

Run:

```bash
python3 scripts/cleanup-generated-and-roster-cruft.py
```

The script removes generated Hugo output and obsolete roster placeholder files that should not be maintained in source.
