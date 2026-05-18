from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedItemSetErrorEnum(proto.Message):
    class FeedItemSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ITEM_SET_REMOVED = 2
        CANNOT_CLEAR_DYNAMIC_FILTER = 3
        CANNOT_CREATE_DYNAMIC_FILTER = 4
        INVALID_FEED_TYPE = 5
        DUPLICATE_NAME = 6
        WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE = 7
        DYNAMIC_FILTER_INVALID_CHAIN_IDS = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
