from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class YoutubeVideoRegistrationErrorEnum(proto.Message):
    class YoutubeVideoRegistrationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VIDEO_NOT_FOUND = 2
        VIDEO_NOT_ACCESSIBLE = 3
        VIDEO_NOT_ELIGIBLE = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
