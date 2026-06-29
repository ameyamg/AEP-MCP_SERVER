#!/usr/bin/env python3
"""Install git hooks from the hooks/ directory into .git/hooks/."""

import shutil
import stat
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
hooks_src = repo_root / "hooks"
hooks_dst = repo_root / ".git" / "hooks"

if not (repo_root / ".git").exists():
    print("Not a git repository. Run 'git init' first.")
    sys.exit(1)

hooks_dst.mkdir(exist_ok=True)

for hook in hooks_src.iterdir():
    if hook.name.startswith("."):
        continue
    dst = hooks_dst / hook.name
    shutil.copy2(hook, dst)
    dst.chmod(dst.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"Installed: .git/hooks/{hook.name}")

print("\nHooks installed. Credential check will run before every commit.")
