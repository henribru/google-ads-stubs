from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FeedItemSetLinkErrorEnum(proto.Message):
    class FeedItemSetLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ID_MISMATCH = 2
        NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
