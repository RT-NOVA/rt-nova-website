#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="rt-nova"

PRODUCTION_BASE_URL="https://rawlingstigersnova.org/"
PREVIEW_BASE_URL="https://rt-nova.workers.dev/"

BRANCH="${WORKERS_CI_BRANCH:-${CF_PAGES_BRANCH:-${CF_BRANCH:-}}}"

echo "Cloudflare branch: ${BRANCH:-unknown}"
echo "Cloudflare Pages URL: ${CF_PAGES_URL:-unknown}"

case "${BRANCH}" in
  main)
    HUGO_BASE_URL="${PRODUCTION_BASE_URL}"
    ;;

  preview)
    HUGO_BASE_URL="${PREVIEW_BASE_URL}"
    ;;

  *)
    HUGO_BASE_URL="${CF_PAGES_URL:-${PREVIEW_BASE_URL}}"
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

if [[ -f scripts/validate-site.sh ]]; then
  bash scripts/validate-site.sh public
fi
