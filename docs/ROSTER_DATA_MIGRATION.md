# Roster Data Migration

This patch moves roster data out of large markdown front matter and into season-based YAML files.

## New structure

```text
data/seasons/2026/rosters/
  13u-black.yaml
  13u-orange.yaml
  11u.yaml

data/seasons/2027/rosters/
  14u-black.yaml
  14u-orange.yaml
  13u.yaml
  12u.yaml
  11u.yaml
  10u.yaml
```

## What stays the same

The Teams page configuration and roster links are unchanged. Existing links such as `/rosters/2026-13u-orange/` continue to work through lightweight markdown route files.

## Why this changed

The roster data is now structured for future Team Central archive/search work while keeping per-team roster editing manageable.


## Cleanup after applying

Zip patches cannot delete existing files from your working tree. After applying this migration, run:

```bash
bash scripts/cleanup-roster-transition-files.sh
```

This removes generated Hugo output and obsolete roster-card/photo transition files.
