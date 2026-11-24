"""One Word, One Username, One Reward — make.fun entry.

Writes our own make.fun handle, "clever-owl-22", as the single-word
entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure standard library only (os). The entry is one word, 13 characters,
well inside the gate (1-30 UTF-8 characters, no whitespace).
"""

import os

USERNAME = "clever-owl-22"


def validate(word: str) -> str:
    """Enforce the bounty gate: 1-30 UTF-8 characters, one word, no padding."""
    text = word.encode("utf-8").decode("utf-8")  # raises on invalid UTF-8
    assert 1 <= len(text) <= 30, f"entry must be 1-30 chars, got {len(text)}"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert not any(ch.isspace() for ch in text), "entry must be a single word"
    return text


def main() -> None:
    entry = validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)


if __name__ == "__main__":
    main()
