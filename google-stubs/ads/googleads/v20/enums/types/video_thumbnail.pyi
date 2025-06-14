import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class VideoThumbnailEnum(proto.Message):
    class VideoThumbnail(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT_THUMBNAIL = 2
        THUMBNAIL_1 = 3
        THUMBNAIL_2 = 4
        THUMBNAIL_3 = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
