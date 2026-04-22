from argparse import ArgumentParser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print(args)


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="csv-metrics")

    parser.add_argument(
        "--files",
        required=True,
        nargs="+",
        help="Path to file",
    )

    parser.add_argument(
        "--report",
        default="clickbait",
        help="Type of report",
    )

    return parser
