from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MediaTypeEnum(proto.Message):
    class MediaType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IMAGE = 2
        ICON = 3
        MEDIA_BUNDLE = 4
        AUDIO = 5
        VIDEO = 6
        DYNAMIC_IMAGE = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
