"""What the Elevator Would Say — make.fun entry.

Writes one original line, in the elevator's own voice, to
/output/entry.txt. Python 3.13, standard library only, deterministic:
the same bytes on every run. No network, no randomness, no input files.
"""

import os

LINE = "I know exactly how much you weigh, and I keep that secret better than your doctor does."

MAX_CHARS = 120


def main() -> None:
    line = LINE.strip()
    assert line, "entry line must not be empty"
    assert len(line) <= MAX_CHARS, f"entry line is {len(line)} chars, over the {MAX_CHARS} cap"
    assert "\n" not in line, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the line, no newline.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == line


if __name__ == "__main__":
    main()
