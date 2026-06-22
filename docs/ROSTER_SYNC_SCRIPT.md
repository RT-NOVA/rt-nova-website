# Roster Sync Script

Use `scripts/sync-roster-pages.py` to generate roster page route stubs from roster YAML data.

## Why this exists

Hugo needs a content page to create a clean URL such as:

```text
/rosters/2026-11u/
```

The roster data itself lives in:

```text
data/seasons/2026/rosters/11u.yaml
```

The sync script lets roster YAML remain the only file you edit manually.

## Normal workflow

Run the script when adding, renaming, or deleting roster data files, or when changing `route_slug`:

```bash
python3 scripts/sync-roster-pages.py
hugo server -D --disableFastRender
```

You do not need to run the script for normal player/staff edits in an existing roster YAML file.

## route_slug

By default, this data file:

```text
data/seasons/2026/rosters/13u-orange.yaml
```

generates:

```text
content/rosters/2026-13u-orange.md
```

Use `route_slug` when the public URL should be different from the data filename:

```yaml
route_slug: "2026-11u"
```

This is useful for term-specific data files, such as keeping Spring 2026 11U at `/rosters/2026-11u/` while adding Fall 2025 11U at `/rosters/2026-11u-fall/`.

## Check mode

```bash
python3 scripts/sync-roster-pages.py --check
```

This exits non-zero if generated markdown route files are out of sync.

## Generated files

Generated route files include this marker:

```yaml
generated_by: sync-roster-pages
```

The script only prunes stale route files that include this marker.
