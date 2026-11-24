#!/usr/bin/env python3
"""Writes one sentence pitching a bizarre startup idea to /output/entry.txt.

The pitch: a service that hires professional arguers to fight couples'
battles for them by phone, so partners pay to stay silent while a stranger
shouts about the dishes. Ridiculous at first glance; a real market (couples
paying to outsource conflict) on the second.
"""

import os

LINE = (
    "We hire professional arguers to have couples' arguments for them by phone, "
    "because partners gladly pay $40 an hour to stay silent while a stranger "
    "shouts about the dishes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
