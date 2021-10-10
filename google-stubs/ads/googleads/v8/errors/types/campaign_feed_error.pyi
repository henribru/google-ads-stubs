from typing import Any

import proto

__protobuf__: Any

class CampaignFeedErrorEnum(proto.Message):
    class CampaignFeedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: int
        CANNOT_CREATE_FOR_REMOVED_FEED: int
        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: int
        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: int
        INVALID_PLACEHOLDER_TYPE: int
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: int
        NO_EXISTING_LOCATION_CUSTOMER_FEED: int
