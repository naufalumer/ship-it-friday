#!/usr/bin/env python3
"""Ship It Friday: write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one git commit message an AI coding agent writes right
before breaking production on a Friday. Standard library only.
One line, no trailing newline, inside the 1-159 character gate.
"""

import os
import sys

ENTRY = "feat: friday deploy at 5pm, tests passed first try so i stopped asking questions"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    data = open(path, "rb").read()
    if not data or len(data) > 159:
        print("entry.txt is outside the 1-159 character gate", file=sys.stderr)
        return 1
    if data != ENTRY.encode("utf-8"):
        print("entry.txt does not match the entry line", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (path, len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
