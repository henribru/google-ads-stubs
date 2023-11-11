from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class MatchingFunctionContextTypeEnum(proto.Message):
    class MatchingFunctionContextType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ITEM_ID = 2
        DEVICE_NAME = 3
        FEED_ITEM_SET_ID = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
