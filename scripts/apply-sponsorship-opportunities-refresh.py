#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for rel in [
    "content/sponsors.md",
    "layouts/partials/page-sponsors.html",
    "data/sponsors.yaml",
]:
    path = root / rel
    if path.exists():
        path.unlink()
        print(f"Removed old sponsorship file: {rel}")

print("Sponsorship opportunities refresh cleanup complete.")
