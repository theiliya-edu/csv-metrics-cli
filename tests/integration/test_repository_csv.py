from decimal import Decimal

import pytest

from csv_metrics.domain.video_metrics import REQUIRED_FIELDS, VideoMetrics
from csv_metrics.infrastructure.mapper import VideoMetricsMapper
from csv_metrics.infrastructure.repositories import CSVVideoMetricsRepository


def make_csv(headers: list[str], data_rows: list[list[str]]) -> str:
    """Build CSV string from headers and rows for testing purposes."""

    header = ",".join(headers)
    lines = "\n".join(",".join(row) for row in data_rows)

    return f"{header}\n{lines}\n"


def test_repo_reads_valid_csv(tmp_path):
    file = tmp_path / "data.csv"

    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "video1,20.2,30,1000,100,3.5\n"
        "video2,11.4,50,2000,200,2.1\n"
    )

    repo = CSVVideoMetricsRepository([file], VideoMetricsMapper())

    data = list(repo.read())

    assert len(data) == 2

    assert data == [
        VideoMetrics(
            title="video1",
            ctr=Decimal("20.2"),
            retention_rate=Decimal("30"),
            views=1000,
            likes=100,
            avg_watch_time=Decimal("3.5"),
        ),
        VideoMetrics(
            title="video2",
            ctr=Decimal("11.4"),
            retention_rate=Decimal("50"),
            views=2000,
            likes=200,
            avg_watch_time=Decimal("2.1"),
        ),
    ]


@pytest.mark.parametrize("missing_field", sorted(REQUIRED_FIELDS))
def test_repo_raises_when_required_column_missing(tmp_path, missing_field):
    """Repository should raise ValueError if any required column is missing."""

    headers = sorted(REQUIRED_FIELDS - {missing_field})

    content = make_csv(headers, [["1"] * len(headers)])

    file = tmp_path / "data.csv"
    file.write_text(content)

    repo = CSVVideoMetricsRepository([file], VideoMetricsMapper())

    with pytest.raises(ValueError, match="missing columns"):
        list(repo.read())


def test_repo_raises_when_headers_missing(tmp_path):
    file = tmp_path / "data.csv"

    # DictReader treats first row as headers, but these are invalid field names
    file.write_text("1,1,1\n2,2,2\n")

    repo = CSVVideoMetricsRepository([file], VideoMetricsMapper())

    with pytest.raises(ValueError, match="missing columns"):
        list(repo.read())


def test_repo_raises_when_file_not_found(tmp_path):
    file = tmp_path / "data.csv"

    repo = CSVVideoMetricsRepository([file], VideoMetricsMapper())

    with pytest.raises(FileNotFoundError):
        list(repo.read())
