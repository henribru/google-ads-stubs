import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ReachPlanNetworkEnum(proto.Message):
    class ReachPlanNetwork(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YOUTUBE = 2
        GOOGLE_VIDEO_PARTNERS = 3
        YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
