from decimal import Decimal

import pytest

from csv_metrics.application.reports import ClickbaitReport
from csv_metrics.application.use_cases import MakeReportUseCase
from csv_metrics.domain.video_metrics import VideoMetrics
from csv_metrics.infrastructure.mapper import VideoMetricsMapper
from csv_metrics.infrastructure.repositories import CSVVideoMetricsRepository


def test_use_case_returns_filtered_and_sorted_data(tmp_path):
    """Use case should read CSV, filter items, and return them sorted by ctr descending."""

    file = tmp_path / "data.csv"

    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "video1,20.2,30,1000,100,3.5\n"  # included: ctr > 15 and retention_rate < 40
        "video2,11.4,50,2000,200,2.1\n"  # excluded: ctr < 15
        "video3,25,20,3000,300,4.0\n"  # included
    )

    use_case = MakeReportUseCase(
        ClickbaitReport(),
        CSVVideoMetricsRepository([file], VideoMetricsMapper()),
    )

    result = use_case.execute()

    assert result == [
        VideoMetrics(
            title="video3",
            ctr=Decimal("25"),
            retention_rate=Decimal("20"),
            views=3000,
            likes=300,
            avg_watch_time=Decimal("4.0"),
        ),
        VideoMetrics(
            title="video1",
            ctr=Decimal("20.2"),
            retention_rate=Decimal("30"),
            views=1000,
            likes=100,
            avg_watch_time=Decimal("3.5"),
        ),
    ]


def test_use_case_raises_value_error(tmp_path):
    """Use case should propagate ValueError from repository."""

    file = tmp_path / "data.csv"

    file.write_text("ctr,retention_rate,views,likes,avg_watch_time\n20,30,1000,100,3.5\n")

    use_case = MakeReportUseCase(
        ClickbaitReport(),
        CSVVideoMetricsRepository([file], VideoMetricsMapper()),
    )

    with pytest.raises(ValueError, match="missing columns"):
        use_case.execute()


def test_use_case_raises_file_not_found_error(tmp_path):
    """Use case should propagate FileNotFoundError from repository."""

    file = tmp_path / "data.csv"

    use_case = MakeReportUseCase(
        ClickbaitReport(),
        CSVVideoMetricsRepository([file], VideoMetricsMapper()),
    )

    with pytest.raises(FileNotFoundError):
        use_case.execute()
