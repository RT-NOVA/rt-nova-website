# RT NOVA Team Central Black Header Toggle Fix

This update removes the visible white selector cap and positions the Current/Upcoming toggle inside the black season header.

Apply from repo root:

```bash
unzip -o rt-nova-team-central-black-inline-toggle-fix.zip -d .
python3 scripts/apply-team-central-black-header-inline-fix.py
hugo server -D
```

Files modified by the script:

- `assets/css/main.css`
- `assets/js/main.js` if present

No data files are modified.
