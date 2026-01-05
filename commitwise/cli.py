import sys

from commitwise import __version__
from commitwise.cli_utils import (
    build_parser,
)
from commitwise.git_utils import (
    get_staged_diff,
    git_commit_with_message,
    confirm_commit,
)
from commitwise.file_source import read_commit_file
from commitwise.ai_source import generate_ai_commit_message
from commitwise.errors import (
    CommitWiseError,
    NoStagedChangesError,
    UserAbortError,
    AIProviderTimeout,
    AIProviderAuthError,
)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # version flag
    if args.version:
        print(f"commitwise {__version__}")
        sys.exit(0)

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

            if not confirm_commit(message):
                print("\n\nCommit aborted.")
                sys.exit(0)

            git_commit_with_message(message)
            return

        # File mode
        if args.file:
            message = read_commit_file(args.file)
            git_commit_with_message(message)
            return

    except UserAbortError:
        print("\nCommit aborted.")
        sys.exit(0)

    except AIProviderTimeout:
        print(
            "\n[X] AI provider timed out.\n\n"
            "This may happen due to a large diff or slow local inference.\n"
            "Try committing smaller changes or another AI provider."
        )
        sys.exit(2)

    except AIProviderAuthError:
        print(
            "\n[X] AI authentication failed.\n\n"
            "Please check your API key configuration."
        )
        sys.exit(3)

    except NoStagedChangesError:
        print(
            "\n[X] No staged changes found.\n\n"
            "Please run `git add` before using CommitWise."
        )
        sys.exit(0)

    except CommitWiseError as e:
        print(f"\n[X] {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"\n[X] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
