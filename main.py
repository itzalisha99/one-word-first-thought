#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that comes
to mind. The word is "aglet" — the little plastic tip on the end of a
shoelace. It is a word most readers never knew existed for a thing they
touch every day: surprising, vivid, specific, and short.
"""

import os

WORD = "aglet"


def validate(word: str) -> None:
    """Mirror the bounty gate: one word, 1-24 chars, no whitespace."""
    if not (1 <= len(word) <= 24):
        raise ValueError(f"word must be 1-24 chars, got {len(word)}")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if word != word.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != WORD:
        raise ValueError("written entry does not match chosen word")


if __name__ == "__main__":
    main()
