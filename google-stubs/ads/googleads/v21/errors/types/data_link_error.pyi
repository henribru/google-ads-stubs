from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class DataLinkErrorEnum(proto.Message):
    class DataLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YOUTUBE_CHANNEL_ID_INVALID = 2
        YOUTUBE_VIDEO_ID_INVALID = 3
        YOUTUBE_VIDEO_FROM_DIFFERENT_CHANNEL = 4
        PERMISSION_DENIED = 5
        INVALID_STATUS = 6
        INVALID_UPDATE_STATUS = 7
        INVALID_RESOURCE_NAME = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
