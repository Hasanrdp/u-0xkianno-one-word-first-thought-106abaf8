#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came
to mind. The program is fully deterministic: no input, no network, no
randomness, no clock — the same bytes on every run.

The word is "snickersnee": an old word for a long knife, and for a fight
fought with such knives. It is surprising (rare and archaic), vivid (two
blades crossing), and carries a spark of wit in its sound — a snicker
and a sneeze folded into one word.
"""

import os

WORD = "snickersnee"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    # Post-write gate: read the file back and confirm it holds exactly
    # the word, non-empty and a single word with no whitespace, so a
    # truncated or empty write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != WORD:
        raise ValueError("written output does not match the word")
    if not written:
        raise ValueError("written output is empty")
    if written.split() != [written]:
        raise ValueError("written output is not a single word")
    print(f"wrote {OUTPUT_PATH}: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
