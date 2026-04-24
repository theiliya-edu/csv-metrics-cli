from dataclasses import dataclass, fields
from decimal import Decimal


@dataclass(frozen=True)
class VideoMetrics:
    title: str
    ctr: Decimal
    retention_rate: Decimal
    views: int
    likes: int
    avg_watch_time: Decimal


REQUIRED_FIELDS = {field.name for field in fields(VideoMetrics)}
