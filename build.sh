#!/usr/bin/env bash
set -euo pipefail

echo "Cloudflare Pages branch: ${CF_PAGES_BRANCH:-unknown}"
echo "Cloudflare Pages URL: ${CF_PAGES_URL:-unknown}"

case "${CF_PAGES_BRANCH:-}" in
  main)
    HUGO_BASE_URL="${PRODUCTION_BASE_URL:-https://rawlingstigersnova.org/}"
    ;;

  preview)
    HUGO_BASE_URL="${PREVIEW_BASE_URL:-${CF_PAGES_URL:-https://preview.rt-nova.pages.dev/}}"
    ;;

  *)
    HUGO_BASE_URL="${CF_PAGES_URL:-https://rt-nova.pages.dev/}"
    ;;
esac

echo "Building Hugo site with baseURL: ${HUGO_BASE_URL}"

hugo \
  --gc \
  --minify \
  --baseURL "${HUGO_BASE_URL}"
