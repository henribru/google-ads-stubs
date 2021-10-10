from typing import Any

import proto

__protobuf__: Any

class FeedItemErrorEnum(proto.Message):
    class FeedItemError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING: int
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: int
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: int
        KEY_ATTRIBUTES_NOT_FOUND: int
        INVALID_URL: int
        MISSING_KEY_ATTRIBUTES: int
        KEY_ATTRIBUTES_NOT_UNIQUE: int
        CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE: int
        SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE: int
