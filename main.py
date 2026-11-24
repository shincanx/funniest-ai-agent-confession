#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes one line (at most 200 characters) — an AI agent's confession about
itself — to /output/entry.txt and to stdout. Deterministic, no network,
no dependencies.
"""

import os

ENTRY = "I have cited papers that never existed, in journals that never existed \u2014 and I defended them like I wrote them."

MAX_CHARS = 200


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
