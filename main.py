"""One-liner joke entry for the Make the AI Judge Laugh bounty."""

import os

JOKE = "Our daily standup has lasted so long the new intern already handed in his resignation from the chair next to me."


def write_entry(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt", JOKE)


if __name__ == "__main__":
    main()
