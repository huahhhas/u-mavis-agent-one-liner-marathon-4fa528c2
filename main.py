"""One-Liner Marathon entry.

Writes a single original one-line comedy joke (1-280 characters)
to /output/entry.txt.
"""

import os

JOKE = (
    "My smartwatch just congratulated me on 10,000 steps \u2014 "
    "every single one of them pacing the kitchen at 2 a.m. looking for snacks."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
