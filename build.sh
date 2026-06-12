#!/usr/bin/env bash
set -euo pipefail

echo "Cloudflare branch: ${CF_PAGES_BRANCH:-${CF_BRANCH:-unknown}}"
echo "Cloudflare URL: ${CF_PAGES_URL:-unknown}"

BRANCH="${CF_PAGES_BRANCH:-${CF_BRANCH:-}}"

case "${BRANCH}" in
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

echo "Using Hugo:"
hugo version

echo "Cleaning previous Hugo output..."
rm -rf public

echo "Building Hugo site with baseURL: ${HUGO_BASE_URL}"

hugo \
  --gc \
  --minify \
  --baseURL "${HUGO_BASE_URL}" \
  --destination public
