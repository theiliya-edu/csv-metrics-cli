from collections.abc import Iterable
from decimal import Decimal

from csv_metrics.application.interfaces import Report
from csv_metrics.domain.video_metrics import VideoMetrics


class ClickbaitReport(Report):
    def __init__(
        self, min_ctr: Decimal = Decimal("15"), max_retention_rate: Decimal = Decimal("40")
    ):
        self.min_ctr = min_ctr
        self.max_retention_rate = max_retention_rate

    def calculate(self, items: Iterable[VideoMetrics]) -> list[VideoMetrics]:
        return sorted(
            (
                el
                for el in items
                if el.ctr > self.min_ctr and el.retention_rate < self.max_retention_rate
            ),
            key=lambda x: x.ctr,
            reverse=True,
        )
