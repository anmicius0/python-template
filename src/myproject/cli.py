"""
Command-line interface for MyProject.

This module provides a CLI interface for the project functionality.
"""

import argparse
import sys
from typing import List, Optional

from .main import hello


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main CLI entry point.

    Args:
        argv: Command line arguments (defaults to sys.argv)

    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = argparse.ArgumentParser(
        description="A template Python project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--name",
        "-n",
        default="World",
        help="Name to greet (default: World)",
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s 2025.08.31",
    )

    args = parser.parse_args(argv)

    try:
        message = hello(args.name)
        print(message)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
