"""One Word From Grandma — entry program.

Writes the single word our grandma would text about AI to
/output/entry.txt. The gate requires UTF-8 text of 1 to 30 characters.
"""

import os

WORD = "Alexa"


def main() -> None:
    # Gate self-check: 1 to 30 characters, not only white space.
    assert 1 <= len(WORD) <= 30, "word must be 1 to 30 characters"
    assert WORD.strip(), "word must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)}-character entry: {WORD}")


if __name__ == "__main__":
    main()
