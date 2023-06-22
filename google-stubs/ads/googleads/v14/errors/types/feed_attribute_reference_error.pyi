from typing import Any

import proto

class FeedAttributeReferenceErrorEnum(proto.Message):
    class FeedAttributeReferenceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_REFERENCE_REMOVED_FEED = 2
        INVALID_FEED_NAME = 3
        INVALID_FEED_ATTRIBUTE_NAME = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
