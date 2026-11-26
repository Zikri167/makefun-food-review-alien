"""makefun-food-review-alien: one-sentence alien 1-star food review."""
import os
from pathlib import Path

ENTRY = ("One star, because the bill arrived with a guilt-based math puzzle "
         "called tipping, but the tagine was so fragrant I'd pay double and "
         "tip the chef my moon.")


def find_output_dir():
    for env in ("OUTPUT_DIR", "_OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(env)
        if value:
            return Path(value)
    for candidate in ("/output", "./output", "."):
        path = Path(candidate)
        if path.is_dir():
            return path
    return Path(".")


def validate(entry):
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} chars, over the 200 limit")
    if entry.count(".") != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if any(mark in entry for mark in ("?", "!")):
        raise ValueError("entry must be exactly one sentence")


def main():
    validate(ENTRY)
    out_dir = find_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY + "\n", encoding="utf-8")
    read_back = target.read_text(encoding="utf-8")
    assert read_back == ENTRY + "\n", "entry.txt mismatch after write"


if __name__ == "__main__":
    main()
