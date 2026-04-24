from csv_metrics.application.interfaces import Report, VideoMetricsRepository
from csv_metrics.domain.video_metrics import VideoMetrics


class MakeReportUseCase:
    def __init__(self, report: Report, repo: VideoMetricsRepository):
        self.report = report
        self.repo = repo

    def execute(self) -> list[VideoMetrics]:
        data = self.repo.read()
        return self.report.calculate(data)
