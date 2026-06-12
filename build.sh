#!/usr/bin/env bash
set -euo pipefail

# Supports both Cloudflare Pages and the newer Workers Builds Git flow.
# Pages provides CF_PAGES_BRANCH / CF_PAGES_URL.
# Workers Builds provides WORKERS_CI_BRANCH. See Cloudflare Workers Builds default env vars.
BRANCH="${CF_PAGES_BRANCH:-${WORKERS_CI_BRANCH:-${CF_BRANCH:-}}}"
DEPLOY_URL="${CF_PAGES_URL:-}"

# Helpful diagnostic output in Cloudflare build logs.
echo "Cloudflare branch: ${BRANCH:-unknown}"
echo "Cloudflare Pages URL: ${DEPLOY_URL:-unknown}"
echo "Workers CI: ${WORKERS_CI:-0}"

case "${BRANCH}" in
  main)
    # Temporarily set PRODUCTION_BASE_URL to https://rt-nova.pages.dev/ or your current Workers URL
    # until rawlingstigersnova.org is actually attached and ready.
    HUGO_BASE_URL="${PRODUCTION_BASE_URL:-https://rawlingstigersnova.org/}"
    ;;

  preview)
    # For Workers preview aliases, this may become something like:
    # https://preview-rt-nova.<your-workers-subdomain>.workers.dev/
    HUGO_BASE_URL="${PREVIEW_BASE_URL:-${DEPLOY_URL:-https://preview.rt-nova.pages.dev/}}"
    ;;

  *)
    HUGO_BASE_URL="${DEPLOY_URL:-${DEFAULT_BASE_URL:-https://rt-nova.pages.dev/}}"
    ;;
esac

# Ensure a trailing slash for Hugo baseURL.
case "${HUGO_BASE_URL}" in
  */) ;;
  *) HUGO_BASE_URL="${HUGO_BASE_URL}/" ;;
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
