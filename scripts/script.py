"""
Command line entry point for the outbound round tracking demo.

run this script with
```
python scripts/script.py 2
```
"""

import argparse
from typing import Sequence

from myPackage import myAnalysisTools


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the script.

    Parameters
    ----------
    argv : Sequence[str] | None
        Optional list of arguments, defaults to `None` to read from sys.argv.

    Returns
    -------
    argparse.Namespace
        Parsed arguments containing the value to increment and log level.
    """
    parser = argparse.ArgumentParser(
        description="Increment a value using the ort.kalman module."
    )
    parser.add_argument(
        "some_value",
        type=float,
        help="Numeric value that will be incremented by 1.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for running the script logic."""
    args = parse_args(argv)

    incremented = myAnalysisTools.add_one(args.some_value)
    print(f"{args.some_value} plus one is {incremented}")


if __name__ == "__main__":
    main()

