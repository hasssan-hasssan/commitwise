import subprocess
import tempfile
import os


def get_staged_diff() -> str:
    """
    Return the staged git diff
    Raises an error if there are no staged changes
    """

    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)

    diff = result.stdout.strip()

    if not diff:
        raise RuntimeError(
            "No staged changes found.\nPlease run `git add` before using CommitWise."
        )
    return diff


def git_commit_with_message(message: str) -> None:
    """
    Perform a git commit using the given commit message.
    The message is written to a temporary file and passed to
    `git commit -F` to preserve formatting exactly.
    """

    if not message or not message.strip():
        raise ValueError("Commit message is empty.")

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
        ) as tmp:
            tmp.write(message.rstrip() + "\n")
            temp_file_path = tmp.name

        subprocess.run(["git", "commit", "-F", temp_file_path], check=True)
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
