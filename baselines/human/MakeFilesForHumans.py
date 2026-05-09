#!/usr/bin/env python3

from __future__ import annotations

import random
from pathlib import Path
from typing import List, Tuple


def get_text_files(folder: Path, limit: int = 100) -> List[Path]:
    """Return up to `limit` .txt files from a folder, sorted by name."""
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    files = sorted(folder.glob("*.txt"))
    random.shuffle(files)
    if len(files) < limit:
        raise ValueError(
            f"Folder '{folder}' contains only {len(files)} .txt files; "
            f"at least {limit} are required."
        )
    return files[:limit]


def read_text_file(path: Path) -> str:
    """Read a text file as UTF-8, falling back safely if needed."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace").strip()


def build_dataset(folder1: Path, folder2: Path, per_folder: int = 100) -> List[Tuple[str, str]]:
    """
    Return a list of (text, folder_name) pairs from two folders.
    """
    files1 = get_text_files(folder1, per_folder)
    files2 = get_text_files(folder2, per_folder)

    dataset: List[Tuple[str, str]] = []

    for file_path in files1:
        dataset.append((read_text_file(file_path), folder1.name))

    for file_path in files2:
        dataset.append((read_text_file(file_path), folder2.name))

    random.shuffle(dataset)
    return dataset


def write_outputs(
    dataset: List[Tuple[str, str]],
    combined_output: Path,
    key_output: Path,
) -> None:
    """Write the numbered texts file and the key file."""
    with combined_output.open("w", encoding="utf-8") as combined_file, \
         key_output.open("w", encoding="utf-8") as key_file:

        for i, (text, folder_name) in enumerate(dataset, start=1):
            combined_file.write(f"{i}. {text}\n\n")
            key_file.write(f"{i}. {folder_name}\n")


def main() -> None:
    # CHANGE THESE PATHS
    folder1 = Path("/Users/jasonserduke/Downloads/ReviewsNewThesholdsMoreDivided/test/high_80")
    folder2 = Path("/Users/jasonserduke/Downloads/ReviewsNewThesholdsMoreDivided/test/low_50")

    combined_output = Path("reviews.txt")
    key_output = Path("key.txt")

    # Optional: set a seed for reproducible shuffling
    # random.seed()

    dataset = build_dataset(folder1, folder2, per_folder=100)
    write_outputs(dataset, combined_output, key_output)

    print(f"Wrote {combined_output}")
    print(f"Wrote {key_output}")


if __name__ == "__main__":
    main()