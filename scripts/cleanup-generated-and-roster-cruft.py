#!/usr/bin/env python3
from pathlib import Path
import shutil

repo = Path.cwd()
paths_to_remove = [
    repo / "public",
    repo / "resources",
    repo / ".hugo_build.lock",
    repo / "static/images/rosters/default-player-silhouette.svg",
]

for path in paths_to_remove:
    if path.is_dir():
        shutil.rmtree(path)
        print(f"removed directory: {path}")
    elif path.exists():
        path.unlink()
        print(f"removed file: {path}")
    else:
        print(f"not present: {path}")
