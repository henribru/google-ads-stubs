from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
