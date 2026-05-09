#!/usr/bin/env python3
"""
Sorting.py

Usage:
    python Sorting.py input_file.txt output_dir

Reads lines formatted as:
    name<TAB>score<TAB>review\\n

Creates one file per review and places it in a score-based directory.
"""

import sys
from pathlib import Path
import uuid

def choose_bucket(score: int) -> str:
    """Return the output subdirectory name for a given score."""
    if score < 50:
        return "low_50"
    if score >= 80:
        return "high_80"
    return "mid_50_80"

def unique_path(directory: Path, base_name: str, ext: str = ".txt") -> Path:
    """Return a Path that does not exist yet by appending a uuid short suffix if needed."""
    candidate = directory / (base_name + ext)
    if not candidate.exists():
        return candidate
    # append short uuid
    suffix = uuid.uuid4().hex[:8]
    return directory / (f"{base_name}_{suffix}" + ext)

def split_file(input_path: Path, output_base: Path, verbose: bool = True) -> None:
    input_path = Path(input_path)
    output_base = Path(output_base)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # create base directories
    for d in ("low_50", "mid_50_80", "high_80"):
        (output_base / d).mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as fh:
        for idx, raw_line in enumerate(fh):
            line = raw_line.rstrip("\n")
            """
            if not line:
                continue  # skip empty lines
            """

            # split into at most 3 parts so review can contain tabs
            parts = line.split("\t", 2)
            if len(parts) < 3:
                if verbose:
                    print(f"Skipping malformed line {idx}: {line!r}")
                continue

            name, score_str, review = parts
            score_str = score_str.strip()

            try:
                # allow float scores but treat by integer threshold
                score = int(score_str)
            except Exception:
                if verbose:
                    print(f"Skipping line {idx} with invalid score '{score_str}': {line!r}")
                continue

            bucket = choose_bucket(score)
            out_dir = output_base / bucket

            # safe filename: index + score
            base_name = f"{idx}_{score}"
            out_file = unique_path(out_dir, base_name, ext=".txt")

            # write review only (change if you want metadata in the file)
            try:
                with out_file.open("w", encoding="utf-8") as outfh:
                    outfh.write(review)
                # if verbose:
                    # print(f"Wrote {out_file} (score={score})")
            except Exception as e:
                print(f"ERROR writing file for line {idx}: {e}", file=sys.stderr)

def main(argv):
    if len(argv) != 3:
        print("Usage: python Sorting.py input_file.txt output_dir")
        return 2
    input_file = Path(argv[1])
    output_dir = Path(argv[2])
    split_file(input_file, output_dir, verbose=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))