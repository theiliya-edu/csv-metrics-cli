from dataclasses import dataclass

from csv_metrics.application.interfaces import Report
from csv_metrics.application.reports import ClickbaitReport


@dataclass(frozen=True)
class ReportConfig:
    report_type: type[Report]
    output_fields: tuple[str, ...]


REPORT_REGISTRY: dict[str, ReportConfig] = {
    "clickbait": ReportConfig(
        report_type=ClickbaitReport,
        output_fields=("title", "ctr", "retention_rate"),
    ),
}
