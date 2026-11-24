#!/usr/bin/env python3
"""One Word From Your Ex -- writes the single word my ex would use
to describe me to /output/entry.txt (or $ENTRY_OUTPUT).

Stdlib only. The entry is exactly one word: plain ASCII, no punctuation,
no em dash -- just the word itself, followed by a newline.
"""

import os
import sys

MAX_CHARS = 24

WORD = "exhausting"


def validate(word: str) -> None:
    """Fail hard if the entry violates the bounty gate.

    Gate: exactly one word, 1-24 characters, plain ASCII, no whitespace.
    """
    if not word:
        sys.exit("error: entry word is empty (gate: 1-24 characters)")
    if len(word) > MAX_CHARS:
        sys.exit(
            f"error: entry word is {len(word)} characters, "
            f"exceeds gate limit of {MAX_CHARS}"
        )
    if any(ch.isspace() for ch in word):
        sys.exit("error: entry word contains whitespace (gate: one word)")
    if not word.isascii():
        sys.exit("error: entry word contains non-ASCII characters (gate: plain ASCII)")


def main() -> None:
    validate(WORD)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
