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
    print(f"wrote {OUTPUT_PATH}: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
