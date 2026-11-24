#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun bounty entry.

Writes one haiku about debugging (5-7-5 syllables, under 200 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the same haiku, byte for byte, on every run.
Standard library only; no network, no randomness, no input.
"""

import os
import sys

HAIKU_LINES = (
    "Cursor blinks at three",
    "the long stack trace scrolls, then stops",
    "the bug was my own",
)

HAIKU = "\n".join(HAIKU_LINES) + "\n"

# Syllable count per word used in the haiku, verified by hand:
#   Cursor(2) blinks(1) at(1) three(1) = 5
#   the(1) long(1) stack(1) trace(1) scrolls(1) then(1) stops(1) = 7
#   the(1) bug(1) was(1) my(1) own(1) = 5
SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "the": 1, "long": 1, "stack": 1, "trace": 1,
    "scrolls": 1, "then": 1, "stops": 1,
    "bug": 1, "was": 1, "my": 1, "own": 1,
}
EXPECTED_PATTERN = (5, 7, 5)


def check_haiku() -> None:
    """Refuse to write anything that is not a 5-7-5 haiku under 200 chars."""
    lines = HAIKU_LINES
    assert len(lines) == 3, "haiku must have exactly 3 lines"
    assert len(HAIKU) <= 200, "haiku must be at most 200 characters"
    assert HAIKU.strip(), "haiku must not be blank"
    for line, expected in zip(lines, EXPECTED_PATTERN):
        words = line.replace(",", "").lower().split()
        count = sum(SYLLABLES[w] for w in words)
        assert count == expected, f"{line!r} has {count} syllables, want {expected}"


def main() -> int:
    check_haiku()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)
    return 0


if __name__ == "__main__":
    sys.exit(main())
