from typing import Any

import proto

class FeedItemErrorEnum(proto.Message):
    class FeedItemError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING = 2
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM = 3
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = 4
        KEY_ATTRIBUTES_NOT_FOUND = 5
        INVALID_URL = 6
        MISSING_KEY_ATTRIBUTES = 7
        KEY_ATTRIBUTES_NOT_UNIQUE = 8
        CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE = 9
        SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
