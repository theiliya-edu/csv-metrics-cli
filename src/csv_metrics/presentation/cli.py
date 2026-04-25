from argparse import ArgumentParser

from csv_metrics.presentation.composition import build_use_case
from csv_metrics.presentation.configs import REPORT_REGISTRY
from csv_metrics.presentation.presenters import ReportPresenter


def main() -> None:
    args = build_parser().parse_args()

    report_config = REPORT_REGISTRY[args.report]

    use_case = build_use_case(args, report_config)

    try:
        data = use_case.execute()
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return
    except ValueError as e:
        print(f"Data error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    report = ReportPresenter.present(data, report_config.output_fields)

    print(report)


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
        choices=list(REPORT_REGISTRY),
        help="Type of report",
    )

    return parser


if __name__ == "__main__":
    main()
