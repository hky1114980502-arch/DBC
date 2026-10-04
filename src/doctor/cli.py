"""Command-line entry point for doctor."""

import argparse

from doctor import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="doctor")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)
    print("Hello from doctor!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
