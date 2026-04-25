from decimal import Decimal

import pytest

from csv_metrics.domain.video_metrics import VideoMetrics
from csv_metrics.presentation.cli import main


@pytest.fixture
def metrics() -> list[VideoMetrics]:
    ctrs = [
        Decimal("15"),
        Decimal("30"),
        Decimal("15.1"),
        Decimal("7.5"),
        Decimal("13.1"),
        Decimal("29"),
    ]
    retention_rates = [
        Decimal("10"),
        Decimal("40"),
        Decimal("39.9"),
        Decimal("11"),
        Decimal("45.5"),
        Decimal("37.1"),
    ]

    return [
        VideoMetrics(
            title=f"video {i}",
            ctr=ctr,
            retention_rate=retention_rate,
            views=1000,
            likes=100,
            avg_watch_time=Decimal("1.1"),
        )
        for i, (ctr, retention_rate) in enumerate(zip(ctrs, retention_rates, strict=True), start=1)
    ]


@pytest.fixture
def cli_runner():
    import sys

    def _run(args: list[str]):
        old_argv = sys.argv.copy()
        sys.argv = ["csv-metrics", *args]

        try:
            main()
        finally:
            sys.argv = old_argv

    return _run
