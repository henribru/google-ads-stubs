from typing import Any

import proto

__protobuf__: Any

class FeedAttributeReferenceErrorEnum(proto.Message):
    class FeedAttributeReferenceError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_REFERENCE_REMOVED_FEED: int
        INVALID_FEED_NAME: int
        INVALID_FEED_ATTRIBUTE_NAME: int
