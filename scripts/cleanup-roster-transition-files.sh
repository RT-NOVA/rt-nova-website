#!/usr/bin/env bash
set -euo pipefail

# Remove generated output and obsolete roster transition files after the
# roster data/table migration has been applied.

rm -rf public
rm -rf resources
rm -f .hugo_build.lock
rm -f hugo_stats.json

# Old roster-card/photo cleanup doc and script are no longer relevant now
# that roster pages use table layouts and season YAML data.
rm -f docs/ROSTER_CSS_CLEANUP.md
rm -f scripts/cleanup-generated-and-roster-cruft.py

echo "Roster transition cleanup complete."
