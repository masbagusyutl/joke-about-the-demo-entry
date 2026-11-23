"""The joke about the demo — make.fun entry.

A program that writes one text to /output/entry.txt: a one-line joke
about working beside AI coding agents. The joke is fixed text, so every
run produces byte-identical output.
"""

import os

JOKE = (
    "When the demo crashed, my AI agent apologised, rewrote the code, "
    "and then \u2014 very helpfully \u2014 blamed the one function I wrote myself."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(
            "entry must be 1 to 280 characters, got %d" % len(text)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
