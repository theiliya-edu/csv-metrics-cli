from abc import ABC, abstractmethod
from collections.abc import Iterable

from csv_metrics.domain.video_metrics import VideoMetrics


class VideoMetricsRepository(ABC):
    @abstractmethod
    def read(self) -> Iterable[VideoMetrics]: ...
