from typing import Any

import proto

class AdGroupFeedErrorEnum(proto.Message):
    class AdGroupFeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 2
        CANNOT_CREATE_FOR_REMOVED_FEED = 3
        ADGROUP_FEED_ALREADY_EXISTS = 4
        CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED = 5
        INVALID_PLACEHOLDER_TYPE = 6
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = 7
        NO_EXISTING_LOCATION_CUSTOMER_FEED = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
