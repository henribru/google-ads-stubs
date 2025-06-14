import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
