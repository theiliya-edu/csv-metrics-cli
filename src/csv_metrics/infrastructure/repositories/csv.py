from collections.abc import Iterable
from csv import DictReader
from pathlib import Path

from csv_metrics.application.interfaces import VideoMetricsRepository
from csv_metrics.domain.video_metrics import REQUIRED_FIELDS, VideoMetrics
from csv_metrics.infrastructure.mapper import VideoMetricsMapper


class CSVVideoMetricsRepository(VideoMetricsRepository):
    def __init__(self, files: Iterable[Path], mapper: VideoMetricsMapper):
        self.files = files
        self.mapper = mapper

    def read(self) -> Iterable[VideoMetrics]:
        for path in self.files:
            yield from self._read_file(path)

    def _read_file(self, path: Path) -> Iterable[VideoMetrics]:
        with open(path, encoding="utf-8", newline="") as f:
            reader = DictReader(f)

            if reader.fieldnames is None:
                raise ValueError(f"{path}: CSV has no header row")

            missing = sorted(REQUIRED_FIELDS - set(reader.fieldnames))

            if missing:
                raise ValueError(f"{path}: missing columns: {', '.join(missing)}")

            for row in reader:
                yield self.mapper.from_dict(row)
