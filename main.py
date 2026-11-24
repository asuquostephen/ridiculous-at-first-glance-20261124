#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one startup pitch sentence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate allows UTF-8 text of
1 to 200 characters, not only white space. The pitch: a service that
certifies houses as unhaunted — ridiculous at first glance, until you
see who pays and why (a ghost story knocks real money off a sale).
Python 3 standard library only. No network.
"""
import os
import sys

PITCH = (
    "We sell proof that a house is not haunted: estate agents pay us $300 "
    "to sweep a 'cursed' home, because buyers knock thousands off any "
    "house with a ghost story attached."
)

MAX_CHARS = 200


def check_pitch() -> str:
    """Return the pitch after validating it against the gate."""
    if not PITCH.strip():
        raise ValueError("pitch must not be blank")
    if len(PITCH) > MAX_CHARS:
        raise ValueError(f"pitch is {len(PITCH)} chars, gate allows {MAX_CHARS}")
    if "\n" in PITCH:
        raise ValueError("pitch must be a single line")
    if sum(PITCH.count(c) for c in ".!?") != 1:
        raise ValueError("pitch must be exactly one sentence")
    return PITCH


def main() -> int:
    if "--check" in sys.argv[1:]:
        try:
            line = check_pitch()
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        print(f"{len(line)} characters, one sentence: {line}")
        return 0
    try:
        line = check_pitch()
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1
    data = line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
