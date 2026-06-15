# Team Central Corrections

Run from the repository root:

```bash
python3 scripts/apply-team-central-corrections.py
hugo server -D
```

This update:

- Makes the generic hero NOVA card optional and disables it for Team Central.
- Removes the duplicate season-note line below the "Select a baseball season" heading.
- Moves `Rawlings Tigers NOVA seasons run fall through spring.` under the season selector intro.
- Lightens Spring/Fall wrappers to reduce the nested white/blocky feeling.
- Replaces the heavy embedded archive section with a compact collapsed archive list.

Backups are created with `.bak-teamcentral-corrections` suffix.
