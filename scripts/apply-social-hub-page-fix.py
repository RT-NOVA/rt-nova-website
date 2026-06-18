#!/usr/bin/env python3
"""Cleanup helper for the Social Hub page/tabs patch.

Run from the repository root after unzipping the patch. It removes folders that
were accidentally created under content/news by the previous ZIP patch.
"""
from pathlib import Path
import shutil

repo = Path.cwd()
remove_paths = [
    repo / "content" / "news" / "content",
    repo / "content" / "news" / "docs",
    repo / "content" / "news" / "layouts",
    repo / "content" / "news" / "assets",
    repo / "content" / "social-hub" / "layouts",
    repo / "content" / "social-hub" / "assets",
]

for path in remove_paths:
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
            print(f"removed {path}")
        else:
            path.unlink()
            print(f"removed {path}")

print("Social Hub misplaced content cleanup complete.")
