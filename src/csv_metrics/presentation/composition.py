from argparse import Namespace
from pathlib import Path

from csv_metrics.application.use_cases import MakeReportUseCase
from csv_metrics.infrastructure.mapper import VideoMetricsMapper
from csv_metrics.infrastructure.repositories import CSVVideoMetricsRepository
from csv_metrics.presentation.configs import ReportConfig


def build_use_case(args: Namespace, report_config: ReportConfig) -> MakeReportUseCase:
    files = [Path(file) for file in args.files]

    repo = CSVVideoMetricsRepository(files, VideoMetricsMapper())
    report = report_config.report_type()

    return MakeReportUseCase(report, repo)
