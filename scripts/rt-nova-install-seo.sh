#!/usr/bin/env bash
set -euo pipefail

# Run from the root of the Hugo repo after unzipping the patch:
#   bash scripts/rt-nova-install-seo.sh

snippet='{{ partial "head/seo.html" . }}'

if grep -R "partial \"head/seo.html\"\|partial \"seo.html\"\|partial \"seo/meta.html\"" layouts >/dev/null 2>&1; then
  echo "SEO partial already appears to be wired into the site. No change made."
  exit 0
fi

# Prefer a head partial when present. Otherwise inject before </head> in baseof.html.
for candidate in \
  layouts/partials/head.html \
  layouts/partials/site-head.html \
  layouts/partials/head/site-head.html \
  layouts/_default/baseof.html \
  layouts/baseof.html
  do
  if [ -f "$candidate" ]; then
    cp "$candidate" "$candidate.bak-seo"
    if grep -qi '</head>' "$candidate"; then
      python3 - "$candidate" "$snippet" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
snippet = sys.argv[2]
text = path.read_text()
idx = text.lower().rfind('</head>')
if idx == -1:
    text = text.rstrip() + "\n" + snippet + "\n"
else:
    text = text[:idx] + "  " + snippet + "\n" + text[idx:]
path.write_text(text)
PY
    else
      printf '\n%s\n' "$snippet" >> "$candidate"
    fi
    echo "Added SEO partial to $candidate"
    echo "Backup saved as $candidate.bak-seo"
    exit 0
  fi
done

echo "Could not find a head/base template to update automatically."
echo "Add this inside the HTML <head> section manually:"
echo "  $snippet"
exit 1
