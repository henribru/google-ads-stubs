from typing import Any

import proto

__protobuf__: Any

class AdGroupFeedErrorEnum(proto.Message):
    class AdGroupFeedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: int
        CANNOT_CREATE_FOR_REMOVED_FEED: int
        ADGROUP_FEED_ALREADY_EXISTS: int
        CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED: int
        INVALID_PLACEHOLDER_TYPE: int
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: int
        NO_EXISTING_LOCATION_CUSTOMER_FEED: int
