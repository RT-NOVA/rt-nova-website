# Team Central Compact Table Tuning

This update tightens the Team Central table layout so the page feels less spread out and less visually broken up.

It appends CSS overrides to `assets/css/main.css` and creates a backup at:

```text
assets/css/main.css.bak-team-table-compact
```

Apply with:

```bash
python3 scripts/apply-team-central-compact-table.py
```

The tuning keeps the themed table direction, but reduces large vertical gaps, large season banner sizing, row height, coach thumbnail size, and link chip size.
