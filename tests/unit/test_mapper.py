from decimal import Decimal

import pytest

from csv_metrics.domain.video_metrics import REQUIRED_FIELDS, VideoMetrics
from csv_metrics.infrastructure.mapper import VideoMetricsMapper


def test_mapper_parses_valid_row():
    mapper = VideoMetricsMapper()

    row = {
        "title": "video",
        "ctr": "20.2",
        "retention_rate": "30",
        "views": "1000",
        "likes": "100",
        "avg_watch_time": "3.5",
    }

    result = mapper.from_dict(row)

    assert result == VideoMetrics(
        title="video",
        ctr=Decimal("20.2"),
        retention_rate=Decimal("30"),
        views=1000,
        likes=100,
        avg_watch_time=Decimal("3.5"),
    )


def test_mapper_empty_values_default_to_zero():
    """Empty or None values should be converted to numeric zero."""

    mapper = VideoMetricsMapper()

    row = {
        "title": "video",
        "ctr": "",
        "retention_rate": "",
        "views": "",
        "likes": "",
        "avg_watch_time": None,
    }

    result = mapper.from_dict(row)

    assert result == VideoMetrics(
        title="video",
        ctr=Decimal("0"),
        retention_rate=Decimal("0"),
        views=0,
        likes=0,
        avg_watch_time=Decimal("0"),
    )


@pytest.mark.parametrize("field", sorted(REQUIRED_FIELDS - {"title"}))
def test_mapper_raises_when_value_invalid(field):
    """Mapper should raise ValueError for non-numeric values in numeric fields."""

    mapper = VideoMetricsMapper()

    row = {  # noqa
        "title": "video",
        "ctr": "1",
        "retention_rate": "1",
        "views": "1",
        "likes": "1",
        "avg_watch_time": "1",
    }

    row[field] = "invalid"

    with pytest.raises(ValueError):
        mapper.from_dict(row)
