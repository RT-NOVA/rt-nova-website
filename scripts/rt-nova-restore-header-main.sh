#!/usr/bin/env bash
set -euo pipefail

git checkout -- layouts/partials/site-header.html assets/css/header-nav.css assets/js/header-nav.js data/homepage.yaml layouts/index.html assets/css/hero-natural-reset.css 2>/dev/null || true
