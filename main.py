#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry (u-0xkianno-one-word-first-thought-106abaf8).

Methodology (see README.md for the full analysis): the entry is exactly one
word, chosen by a criteria-ordered round-robin over four finalists against
the judge's published brief (surprise > vividness > wit/sound/double meaning
> chosen-not-generic). Winner: "syzygy" — 6 bytes, no trailing newline.

Writes the word to /output/entry.txt, byte-exact. Deterministic, stdlib only,
no network, no environment reads, no secrets.
"""

import os

WORD = "syzygy"  # 6 chars, within the 1-24 char gate; one word, no whitespace

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Binary write: exactly the word, no trailing newline, so the file is
    # byte-identical to the word itself and cannot collide with a padded form.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))
    print(f"wrote {OUTPUT_PATH} ({len(WORD)} bytes): {WORD}")


if __name__ == "__main__":
    main()
