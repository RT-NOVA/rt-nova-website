# v9.1 Build Fix Notes

This package fixes two issues found in v9 when running Hugo 0.163:

1. `data/homepage.yaml` had an unquoted value containing a colon. YAML treats `:` as a mapping delimiter unless the value is quoted, so the intro field is now quoted.
2. `layouts/partials/site-header.html` now safely defaults navigation lists to empty slices before sorting. This prevents header rendering from failing if a data key is missing or temporarily invalid during local edits.

Validation performed before packaging:

```bash
python3 - <<'PY'
import yaml, pathlib
for p in pathlib.Path('data').glob('*.yaml'):
    yaml.safe_load(p.read_text())
    print('OK', p)
PY
./scripts/validate-local-assets.sh
grep -R "cdn-app\\.teamlinkt\\.com" -n . --exclude-dir=.git
```
