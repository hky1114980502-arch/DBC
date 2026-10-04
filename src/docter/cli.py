"""Command-line entry point for docter."""

import argparse

from docter import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="docter")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)
    print("Hello from docter!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
