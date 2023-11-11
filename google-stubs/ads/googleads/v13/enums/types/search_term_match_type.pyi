from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SearchTermMatchTypeEnum(proto.Message):
    class SearchTermMatchType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BROAD = 2
        EXACT = 3
        PHRASE = 4
        NEAR_EXACT = 5
        NEAR_PHRASE = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
