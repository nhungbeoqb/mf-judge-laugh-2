#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The entry program writes a single line (at most 200 characters) to
/output/entry.txt. The line is fixed: no randomness, no time, no
network, so every run writes byte-identical output.
"""

import os

LINE = "I shipped a bug so charming that users named it, gave it fan art, and now I spend my days babysitting a mistake with better job security than me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
