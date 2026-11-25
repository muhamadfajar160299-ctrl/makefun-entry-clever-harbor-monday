"""One Star for Monday: write a one-star review of Monday as a restaurant.

The entry is a single plain-text line (18 words): a diner complains the
waiter seated them at Monday, served cold coffee, then billed them for the
whole week. Written to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline, mode 0644, stdlib only.
"""

import os

ENTRY = "One star. The waiter seated me at Monday, served cold coffee, then billed me for the entire week."


def main():
    if not ENTRY.strip():
        raise SystemExit("entry is empty")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write entry.txt: {exc}")


if __name__ == "__main__":
    main()
