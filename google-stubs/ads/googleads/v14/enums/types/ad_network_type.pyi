from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdNetworkTypeEnum(proto.Message):
    class AdNetworkType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH = 2
        SEARCH_PARTNERS = 3
        CONTENT = 4
        YOUTUBE_SEARCH = 5
        YOUTUBE_WATCH = 6
        MIXED = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
