from typing import Any

import proto

class CampaignFeedErrorEnum(proto.Message):
    class CampaignFeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 2
        CANNOT_CREATE_FOR_REMOVED_FEED = 4
        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED = 5
        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED = 6
        INVALID_PLACEHOLDER_TYPE = 7
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = 8
        NO_EXISTING_LOCATION_CUSTOMER_FEED = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
