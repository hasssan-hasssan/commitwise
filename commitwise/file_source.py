from pathlib import Path


def read_commit_file(path: str) -> str:
    """
    Read a commit message from a text file and return it exactly as written.
    Preserves formatting, newlines, spacing, and punctuation
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Commit message file not found: {path}")

    if not file_path.is_file():
        raise ValueError(f"Provided path is not a file: {path}")

    content = file_path.read_text(encoding="utf-8")

    if not content.strip():
        raise ValueError("Commit message file is empty.")

    # Do NOT modify formatting.
    # Only ensure there is no excessive trailing whitespace at the end.
    return content.rstrip()
