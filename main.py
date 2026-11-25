#!/usr/bin/env python3
"""Make the AI Judge Laugh - entry v1.

Writes a single one-line office-life joke to /output/entry.txt.
"""

import os

JOKE = "Our daily standup has lasted so long the new intern already handed in his resignation from the chair next to me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
