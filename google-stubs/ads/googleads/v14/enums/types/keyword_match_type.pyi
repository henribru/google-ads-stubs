from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class KeywordMatchTypeEnum(proto.Message):
    class KeywordMatchType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXACT = 2
        PHRASE = 3
        BROAD = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
