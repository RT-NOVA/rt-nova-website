# Team Central Card Refresh

Run from the repository root:

```bash
python3 scripts/apply-team-card-social-style.py
hugo server -D
```

This update keeps the Team Central data model the same, but refreshes the visual treatment:

- Team cards become rounded and softer, closer to the Social Hub card style.
- Team cards get subtle shadows, better internal spacing, and rounded link chips.
- Spring/Fall wrappers are kept lighter so the page feels less blocky.
- The season selector and season overview get softer rounded edges.
- The old heavy embedded archive block is replaced with a compact archive expander when the original archive block is present.
- The generic NOVA hero card is hidden on Team Central if it is still present.

Backups are created with `.bak-team-card-refresh` suffix.
