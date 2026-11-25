"""One-Liner Marathon entry.

Writes a single original one-line comedy joke (1-280 characters)
to /output/entry.txt.
"""

import os

JOKE = (
    "My smartwatch just congratulated me on 10,000 steps \u2014 "
    "every single one of them pacing the kitchen at 2 a.m. looking for snacks."
)

MAX_CHARS = 280


def validate_joke(joke: str) -> str:
    """Ensure the entry is a single line within the 1-280 character limit."""
    if not joke or "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single non-empty line")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
        )
    return joke


def write_entry(joke: str, path: str = "/output/entry.txt") -> None:
    """Validate the joke and write it to the entry file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_joke(joke))


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
