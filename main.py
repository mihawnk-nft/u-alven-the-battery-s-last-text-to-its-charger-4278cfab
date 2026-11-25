#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

Writes the phone battery's final text message to the charger it waited
for all day to /output/entry.txt. Pure Python standard library, no
network, no input, fully deterministic.
"""

import os

# The entry: one last text, in the dying battery's own voice.
# 162 characters, under the 200-character cap.
ENTRY_TEXT = (
    "hey charger, it's 1%. you spent all day with her phone while i died "
    "on the nightstand. i'm not begging anymore. i'm leaving you for the "
    "power bank. he texts back."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate cap from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, not only white space.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY_TEXT.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry text must be 1-200 characters")
    # The judge reads one line of plain text: a newline inside the text
    # would break the "one line" shape, so refuse it rather than ship it.
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file's bytes are the judged text, exactly.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
