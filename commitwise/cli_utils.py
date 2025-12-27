import argparse
import os
import sys


def build_parser() -> argparse.ArgumentParser:
    """
    Defines and return all command-line flags for the CommitWise CLI.

    Flags:
        --version, -V
            Display the currently installed commitwise version.

        --ai
            Generate a commit message using AI.

        --file PATH
            Read a commit message from a text file and commit it
            exactly as written, preserving formatting.

    Returns:
        argparser.ArgumentParser: Configured parser with all CLI flags.
    """

    parser = argparse.ArgumentParser(
        prog="commitwise",
        description="CommitWise - Smart Git commits, wisely.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--version",
        "-V",
        action="store_true",
        help="Display the version of commitwise that is currently installed.",
    )

    parser.add_argument(
        "--ai",
        action="store_true",
        help=(
            "Generate commit message using AI.\n"
            "Automatically uses OpenAI if OPENAI_APP_KEY is set,\n"
            "otherwise falls back to a local model (Ollama)."
        ),
    )

    parser.add_argument(
        "--file",
        metavar="PATH",
        help=(
            "Read commit message from a text file and commit it\n"
            "exactly as written (preserves formatting)."
        ),
    )

    return parser


def read_single_key() -> str:
    """
    Reads a single keypress from the user without requiring Enter.

    Works cross-platform:
        - Windows: uses msvcrt.getch()
        - Linux/macOS: uses termios and tty to set raw input mode.

    Returns:
        str: The pressed key as a lowercase string.
    """

    if os.name == "nt":
        import msvcrt

        return msvcrt.getch().decode("utf-8", errors="ignore").lower()
    else:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
