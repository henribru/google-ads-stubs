from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class VideoThumbnailEnum(proto.Message):
    class VideoThumbnail(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT_THUMBNAIL = 2
        THUMBNAIL_1 = 3
        THUMBNAIL_2 = 4
        THUMBNAIL_3 = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
