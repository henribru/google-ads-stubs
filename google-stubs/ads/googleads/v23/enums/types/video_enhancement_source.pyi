from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class VideoEnhancementSourceEnum(proto.Message):
    class VideoEnhancementSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADVERTISER = 2
        ENHANCED_BY_GOOGLE_ADS = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
