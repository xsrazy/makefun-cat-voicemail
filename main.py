#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Writes one voicemail greeting, recorded by a cat named Beans, to
/output/entry.txt. The greeting is 113 characters, inside the 120
character limit of the bounty.

Why this line won the head-to-head selection (10 candidates):
it reads as a real voicemail (greeting, name, "leave a message after
the beep"), it stacks two behaviours only a cat would do (pushing a
phone off a counter, then napping on it), the cat speaks in first
person with a clear attitude, and the punch lands before the beep
line, so it works spoken aloud in a few seconds.
"""

import os

MAX_CHARS = 120

GREETING = (
    "Hi, this is Beans. I pushed your phone off the counter and now "
    "I'm napping on it. Leave a message after the beep."
)


def validate(text):
    """Check the greeting fits the bounty gate: 1 to 120 characters."""
    if not text or text.isspace():
        raise ValueError("greeting must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "greeting is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    return text


def write_entry(text, output_dir):
    """Write the greeting as plain UTF-8 text, no trailing newline.

    The gate counts every character in the file, so the file holds
    exactly the greeting and nothing else.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    text = validate(GREETING)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(text, output_dir)


if __name__ == "__main__":
    main()
