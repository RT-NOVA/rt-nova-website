#!/usr/bin/env bash
set -euo pipefail

ICON_DIR="assets/icons/svgrepo-icooon-mono"
mkdir -p "${ICON_DIR}"

download_icon() {
  local id="$1"
  local name="$2"
  local url="https://staging.svgrepo.com/download/${id}/${name}.svg"
  local output="${ICON_DIR}/${name}.svg"

  echo "Downloading ${name} from ${url}"
  curl -fsSL "${url}" -o "${output}"

  # Normalize common SVG Repo black fills to currentColor so CSS controls color.
  # This keeps the icons matching the orange/white card style.
  perl -0pi -e 's/fill="#[0-9A-Fa-f]{3,6}"/fill="currentColor"/g; s/stroke="#[0-9A-Fa-f]{3,6}"/stroke="currentColor"/g; s/fill="black"/fill="currentColor"/g; s/stroke="black"/stroke="currentColor"/g' "${output}"
}

download_icon "480625" "helmet-2"
download_icon "480638" "bat-4"
download_icon "480475" "whistle-1"
download_icon "480629" "baseball-stadium-1"

echo "Done. Icons saved to ${ICON_DIR}"
