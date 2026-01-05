import subprocess
import tempfile
import os

from commitwise.cli_utils import read_single_key
from commitwise.errors import NoStagedChangesError


def get_staged_diff() -> str:
    """
    Return the staged git diff
    Raises an error if there are no staged changes
    """

    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)

    diff = result.stdout.strip()

    if not diff:
        raise NoStagedChangesError("No staged changes found.")
    
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

        # subprocess.run(["git", "commit", "-F", temp_file_path], check=True)
        result = subprocess.run(
            ["git", "commit", "-F", temp_file_path],
            capture_output=True,
            text=True,
        ).stdout.strip()

        output_message = (
            f"\n\n[✔] Commit created successfully. More details:\n\n{result}"
        )

        print(output_message)

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)


def confirm_commit(message: str) -> bool:
    """
    Confirm the suggested commit message.
    """
    print("\nProposed commit message:\n")
    print("-" * 40)
    print(message.strip())
    print("-" * 40)
    print("\nCommit this message? [y/n] ", end="", flush=True)

    while True:
        key = read_single_key()
        if key == "y":
            return True

        if key == "n":
            return False
