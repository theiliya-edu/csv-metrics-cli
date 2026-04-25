from decimal import Decimal

from csv_metrics.application.reports import ClickbaitReport


def test_clickbait_report_filters_and_sorts(metrics):
    """Report should filter items by ctr/retention_rate and sort by ctr descending."""
    report = ClickbaitReport()
    result = report.calculate(metrics)

    expected = [item for item in metrics if item.ctr > 15 and item.retention_rate < 40]
    expected = sorted(expected, key=lambda x: x.ctr, reverse=True)

    assert result == expected


def test_clickbait_report_returns_empty_when_no_match(metrics):
    report = ClickbaitReport(min_ctr=Decimal("1000"))
    result = report.calculate(metrics)

    assert result == []
