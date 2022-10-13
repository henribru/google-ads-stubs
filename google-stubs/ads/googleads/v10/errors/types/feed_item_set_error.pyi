from typing import Any

import proto

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
