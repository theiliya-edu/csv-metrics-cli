from abc import ABC, abstractmethod
from collections.abc import Iterable

from csv_metrics.domain.video_metrics import VideoMetrics


class Report(ABC):
    @abstractmethod
    def calculate(self, items: Iterable[VideoMetrics]) -> list[VideoMetrics]: ...
