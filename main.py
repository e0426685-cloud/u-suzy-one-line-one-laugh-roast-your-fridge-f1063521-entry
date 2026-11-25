#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single funny one-line roast of my own fridge to
/output/entry.txt. Standard library only.

The roast mocks one specific, recognisable detail — the ancient tub of
sauce living in the fridge — and pays off with a twist in the last few
words. It reads cleanly aloud as one line.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# The roast, split into clauses so the line reads as one sentence but
# stays easy to tweak word by word.
LINE_PARTS = (
    "My fridge hums like it runs a nightclub, but the only regular ",
    "inside is a tub of sauce so old it remembers when the milk ",
    "was still fresh.",
)


def build_line() -> str:
    """Join the roast clauses into the final single-line entry."""
    return "".join(LINE_PARTS).strip()


def validate(line: str) -> bool:
    """Check the entry line against the competition gate.

    Returns True only when the line is a single non-blank line of
    1-200 characters that mentions the fridge, so a bad line is
    caught here instead of reaching the grader.
    """
    if not line or not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if not 1 <= len(line) <= MAX_CHARS:
        return False
    if "fridge" not in line.lower():
        return False
    return True


def write_entry(line: str) -> None:
    """Self-check then write one line of 1-200 chars to entry.txt."""
    assert validate(line), "entry failed validation: %r" % line
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


def main() -> None:
    line = build_line()
    if not validate(line):
        raise SystemExit("entry line failed validation")
    write_entry(line)


if __name__ == "__main__":
    main()
