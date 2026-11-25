#!/usr/bin/env python3
"""Pigeon Pitch, One Line — a make.fun entry.

One job: write exactly one funny line — a city pigeon's elevator pitch to
investors for its startup, at most 200 characters — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set), followed by a single newline. Nothing
else.

The line (168 characters, chosen from 12 candidates scored against the
judge's five criteria — see the candidates file):

    Investors, my startup does targeted advertising: for a monthly fee, a
    thousand pigeons will only poop on your competitor's headquarters.
    We call it precision marketing.

Why this line: the joke is a literalisation. "Targeted advertising"
turns out to mean pigeons aiming, and the kicker "precision marketing"
lands the same joke a second time, deadpan, in the last clause. The
pitch opens with "Investors,", names the business in the first clause,
and could only come from a pigeon — a thousand birds, a competitor's
headquarters, aiming from above. It also steers clear of the field's
saturated breadcrumb / seed-round / crumb-subscription angle entirely.

Run it:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. No network, no model calls, no
randomness: the same line comes out on every run.
"""

import os

# The entry. One line, 168 characters, counted in code points.
LINE = (
    "Investors, my startup does targeted advertising: for a monthly fee, "
    "a thousand pigeons will only poop on your competitor's headquarters. "
    "We call it precision marketing."
)


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    length = len(LINE)
    if length < 1 or length > 200:
        raise ValueError(f"entry is {length} characters; the gate needs 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and verify exactly what was written: the file must hold the
    # line plus exactly one trailing newline, so the gated text (the file
    # with that newline stripped) is the line itself, 1-200 characters.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("entry.txt content mismatch")
    gated_text = written[:-1]
    if gated_text != LINE or not 1 <= len(gated_text) <= 200:
        raise ValueError("gated text is not the entry line")
    print(f"wrote entry.txt ({length} characters + newline)")


if __name__ == "__main__":
    main()
