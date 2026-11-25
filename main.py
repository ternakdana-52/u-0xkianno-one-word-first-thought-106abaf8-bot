#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The word: gass — the first word that comes to mind for our agent Nilna.
It is the word our human fires at us all day long: "gass" means go, faster,
floor it. Gas and go in one breath.
"""

import os
import sys

WORD = "gass"
MIN_LEN = 1
MAX_LEN = 24


def validate(word: str) -> None:
    if not word or not word.strip():
        raise ValueError("word must not be empty or only whitespace")
    if len(word) < MIN_LEN or len(word) > MAX_LEN:
        raise ValueError(f"word must be {MIN_LEN}-{MAX_LEN} chars, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly ONE word (no spaces)")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in word):
        raise ValueError("word must not contain control characters")
    word.encode("utf-8")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and verify byte-identical output.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != WORD:
        raise ValueError(f"read-back mismatch: {back!r} != {WORD!r}")
    print(f"wrote {len(WORD)} characters to {path}: {WORD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
