from collections.abc import Mapping
from decimal import Decimal, InvalidOperation

from csv_metrics.domain.video_metrics import VideoMetrics


class VideoMetricsMapper:
    def from_dict(self, row: Mapping[str, str]) -> VideoMetrics:
        return VideoMetrics(
            title=row["title"],
            ctr=self._to_decimal(row["ctr"]),
            retention_rate=self._to_decimal(row["retention_rate"]),
            views=self._to_int(row["views"]),
            likes=self._to_int(row["likes"]),
            avg_watch_time=self._to_decimal(row["avg_watch_time"]),
        )

    @staticmethod
    def _to_decimal(value: str) -> Decimal:
        if not value:
            return Decimal("0")
        try:
            return Decimal(value)
        except (ValueError, TypeError, InvalidOperation) as e:
            raise ValueError(f"Invalid decimal value: {value}") from e

    @staticmethod
    def _to_int(value: str) -> int:
        if not value:
            return 0
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid int value: {value}") from e
