#!/usr/bin/env bash
set -euo pipefail

git checkout origin/main -- layouts/partials/site-footer.html
rm -f assets/css/footer-brick.css

echo "Restored footer from origin/main and removed footer-brick.css."
