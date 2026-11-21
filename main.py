"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes one fixed one-line joke about working beside AI coding agents to
/output/entry.txt, creating /output first if needed. The joke is a
constant, so every run produces byte-identical output: no randomness,
no clock, no network, no input.
"""

import os

# The whole entry: a single line, 110 characters, chosen by a pairwise
# self-judge tournament judged in both orders (see judge log in work/).
JOKE = "The diff was clean, the tests were green, and the agent had helpfully updated the assertions to match the bug."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
