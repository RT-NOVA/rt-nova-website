# Team Central Compact Table Tuning

This update tightens the Team Central table layout so the page feels less spread out and less visually broken up.

It appends CSS overrides to `assets/css/main.css` and creates a backup at:

```text
assets/css/main.css.bak-team-table-compact
```

Apply with:

```bash
> Historical note: the one-time migration script referenced here was removed after its changes were applied. The current source and Git history are authoritative.
```

The tuning keeps the themed table direction, but reduces large vertical gaps, large season banner sizing, row height, coach thumbnail size, and link chip size.
