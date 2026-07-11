#!/usr/bin/env bash
set -euo pipefail

git checkout origin/main -- \
  layouts/partials/site-header.html \
  layouts/partials/site-footer.html

rm -f assets/css/header-scroll-refresh.css assets/js/header-scroll-refresh.js

echo "Restored header/footer files from origin/main and removed scroll refresh assets."
