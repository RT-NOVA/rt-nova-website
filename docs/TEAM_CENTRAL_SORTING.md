# Team Central Sorting

Team rows are sorted by `sort_order` in `data/teams.yaml`.

The current convention is:

- Older age groups appear first.
- Within the same age group, Black appears before Orange.
- Lower `sort_order` values appear first.

Suggested values:

```yaml
14U Black: 860
14U Orange: 861
13U Black: 870
13U Orange: 871
13U: 872
12U: 880
11U: 890
10U: 900
```

Example:

```yaml
- name: "13U Black"
  sort_order: 870
```

If a new team is added, include a `sort_order` value so it appears in the expected Team Central order.
