from collections.abc import Iterable

from tabulate import tabulate

from csv_metrics.domain.video_metrics import VideoMetrics


class ReportPresenter:
    @staticmethod
    def present(items: list[VideoMetrics], fields: Iterable[str]) -> str:
        return tabulate(
            ({field: getattr(item, field) for field in fields} for item in items),
            headers="keys",
            tablefmt="grid",
        )
