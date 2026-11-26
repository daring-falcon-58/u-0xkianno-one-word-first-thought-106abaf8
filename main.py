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

# Import-time gate self-check: the entry word must pass the sealed gate
# (1-24 chars, single word, valid UTF-8, non-blank) before anything runs.
if not (1 <= len(WORD) <= 24 and WORD.strip() and len(WORD.split()) == 1):
    raise ValueError("entry word fails the 1-24 char single-word gate")
WORD.encode("utf-8")  # raises UnicodeEncodeError if the word is not valid UTF-8

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Binary write: exactly the word, no trailing newline, so the file is
    # byte-identical to the word itself and cannot collide with a padded form.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))
    # Write-back verification: read the file back and compare bytes, so a
    # truncated or altered write fails loudly instead of shipping silently.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise RuntimeError(
            f"write-back mismatch in {OUTPUT_PATH}: {written!r} != {WORD.encode('utf-8')!r}"
        )
    print(f"wrote {OUTPUT_PATH} ({len(WORD)} bytes): {WORD}")


if __name__ == "__main__":
    main()
