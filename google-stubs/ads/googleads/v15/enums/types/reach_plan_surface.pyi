from typing import Any

import proto

class ReachPlanSurfaceEnum(proto.Message):
    class ReachPlanSurface(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IN_FEED = 2
        IN_STREAM_BUMPER = 3
        IN_STREAM_NON_SKIPPABLE = 4
        IN_STREAM_SKIPPABLE = 5
        SHORTS = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
