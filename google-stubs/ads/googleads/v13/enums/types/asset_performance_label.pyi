from typing import Any

import proto

class AssetPerformanceLabelEnum(proto.Message):
    class AssetPerformanceLabel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        LEARNING = 3
        LOW = 4
        GOOD = 5
        BEST = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
