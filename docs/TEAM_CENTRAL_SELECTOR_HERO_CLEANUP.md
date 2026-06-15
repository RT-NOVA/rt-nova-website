# Team Central selector / hero cleanup

This patch removes the duplicate Team Central intro block below the hero and moves the helper copy into the white Select Season card.

It also shortens the hero intro by removing the fall/spring season explanation and forces the current season to load first by setting `default_season: "2026"` in `data/teams.yaml`.

Apply with:

```bash
python3 scripts/apply-team-central-selector-hero-cleanup.py
```
