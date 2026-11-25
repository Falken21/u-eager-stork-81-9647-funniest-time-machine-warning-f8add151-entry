"""Entry for make.fun: Funniest Time Machine Warning Label.

Competition: u-eager-stork-81-9647-funniest-time-machine-warning-f8add151
Writes the one-line warning label to /output/entry.txt with no
trailing newline. Python 3 standard library only.
"""

import os

MAX_CHARS = 120  # the competition gate: 1 to 120 characters

WARNING_LINE = "WARNING: Do not step on butterflies."
LIABILITY_LINE = (
    "We accept no liability for altered elections, "
    "unborn grandparents, or Tuesdays."
)


def build_entry() -> str:
    """Assemble the label in deadpan safety-notice voice.

    The hazard is real (the butterfly effect), the phrasing is a
    genuine liability waiver, and the surprise is saved for the
    last word.
    """
    text = WARNING_LINE + " " + LIABILITY_LINE
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry outside the 1-120 character gate")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(build_entry())


if __name__ == "__main__":
    main()
