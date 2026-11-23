#!/usr/bin/env python3
"""Write exactly one word to /output/entry.txt.

The word is the single word grandma would text about AI: "robot".
Grandma does not say "AI" - she calls it the robot.

Deterministic: every run writes the exact same bytes.
Standard library only, no network access.
"""

import os
import sys

WORD = "robot"


def validate(word: str) -> None:
    """Check the word is exactly one word of non-whitespace text."""
    if not word:
        raise ValueError("word must not be empty")
    if word != word.strip():
        raise ValueError("word must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace of any kind")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")


def main() -> int:
    validate(WORD)
    data = WORD.encode("utf-8")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify: the file must contain exactly the word,
    # byte for byte, with no trailing newline added by accident.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("entry.txt does not contain exactly the word")
    return 0


if __name__ == "__main__":
    sys.exit(main())
