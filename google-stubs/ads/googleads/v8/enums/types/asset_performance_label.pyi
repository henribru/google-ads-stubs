from typing import Any

import proto

__protobuf__: Any

class AssetPerformanceLabelEnum(proto.Message):
    class AssetPerformanceLabel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        LEARNING: int
        LOW: int
        GOOD: int
        BEST: int
