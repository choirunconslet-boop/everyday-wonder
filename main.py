"""One sentence of everyday wonder for the make.fun bounty
'Everyday Wonder, Two Days to Find the Line'.

Writes a single sentence (at most 200 characters) about a small
moment of wonder in everyday life to /output/entry.txt.
"""

import os

LINE = (
    "At 3 a.m. my fridge hummed in the same key as the rain, "
    "and the kitchen became a duet."
)


def main():
    # Gate: the scorer only accepts UTF-8 text of 1 to 200 characters,
    # not only white space, as a single line. Refuse to write otherwise
    # rather than submitting an invalid entry.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
