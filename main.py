#!/usr/bin/env python3
"""Write the one-line office joke to /output/entry.txt.

Entry (70 chars, limit 200): the team held a whole meeting about the dead
office plant, and the meeting changed nothing — the plant is still dead.
One concrete office detail (the dead plant everyone walks past) plus a
surprising turn (a meeting was held about it, and it solved nothing).
Tight, one line, reads cleanly aloud in one breath, and needs no
explanation: the laugh is the meeting itself, solemnly convened for a
plant that stayed dead.
"""
import os

ENTRY = "We held a meeting about the dead office plant. The plant is still dead."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
