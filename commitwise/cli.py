import argparse
import sys

from commitwise.git_utils import (
    get_staged_diff,
    git_commit_with_message,
)
from commitwise.file_source import read_commit_file
from commitwise.ai_source import generate_ai_commit_message


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="commitwise",
        description="CommitWise - Smart Git commits, wisely.",
        formatter_class=argparse.RawTextHelpFormatter,
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


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # [X] both flags used
    if args.ai and args.file:
        parser.error("Use either --ai or --file, not both.")

    # [X] no mode selected
    if not args.ai and not args.file:
        parser.print_help()
        sys.exit(0)

    try:
        # AI mode
        if args.ai:
            diff = get_staged_diff()
            message = generate_ai_commit_message(diff)
            git_commit_with_message(message)
            return

        # File mode
        if args.file:
            message = read_commit_file(args.file)
            git_commit_with_message(message)
            return
    except Exception as e:
        print(f"\n [X] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
