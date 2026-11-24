"""Two Days of Quiet Dread — backup angle entry.

Writes one single-line PR approval to /output/entry.txt.
The line is a reviewer approving code they have read three
times without ever understanding what it does.
"""
import os

LINE = "Approved. The code is fine, but I have read it three times and I still do not know what it does."

MAX_CHARS = 140


def write_entry(path):
    """Write the approval as exactly one line of UTF-8 text."""
    if len(LINE) > MAX_CHARS or "\n" in LINE:
        raise ValueError("entry must be a single line of at most 140 characters")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
