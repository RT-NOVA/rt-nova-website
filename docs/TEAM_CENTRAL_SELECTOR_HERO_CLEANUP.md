# Team Central selector / hero cleanup

This patch removes the duplicate Team Central intro block below the hero and moves the helper copy into the white Select Season card.

It also shortens the hero intro by removing the fall/spring season explanation and forces the current season to load first by setting `default_season: "2026"` in `data/seasons/<season-id>/teams.yaml`.

Apply with:

```bash
> Historical note: the one-time migration script referenced here was removed after its changes were applied. The current source and Git history are authoritative.
```
