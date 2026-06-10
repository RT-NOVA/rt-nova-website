#!/usr/bin/env bash
set -euo pipefail

rm -rf public resources .hugo_build.lock

if grep -R "cdn-app\.teamlinkt\.com" -n . --exclude-dir=.git; then
  echo "ERROR: Found old platform CDN references." >&2
  exit 1
fi

python3 - <<'PY'
import pathlib, re, sys
missing=[]
for p in list(pathlib.Path('data').rglob('*.yaml'))+list(pathlib.Path('content').rglob('*.md'))+list(pathlib.Path('layouts').rglob('*.html')):
    text=p.read_text(errors='ignore')
    for ref in re.findall(r'/images/teamlinkt/[^\s"\'<>)]+' , text):
        if not pathlib.Path('static'+ref).exists():
            missing.append((str(p), ref))
if missing:
    for p, ref in missing:
        print(f'MISSING: {p}: {ref}')
    sys.exit(1)
print('OK: no old CDN references and all local /images/teamlinkt/ assets exist.')
PY
