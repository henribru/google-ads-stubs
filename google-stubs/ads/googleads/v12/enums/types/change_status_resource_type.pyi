from typing import Any

import proto

class ChangeStatusResourceTypeEnum(proto.Message):
    class ChangeStatusResourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP = 3
        AD_GROUP_AD = 4
        AD_GROUP_CRITERION = 5
        CAMPAIGN = 6
        CAMPAIGN_CRITERION = 7
        FEED = 9
        FEED_ITEM = 10
        AD_GROUP_FEED = 11
        CAMPAIGN_FEED = 12
        AD_GROUP_BID_MODIFIER = 13
        SHARED_SET = 14
        CAMPAIGN_SHARED_SET = 15
        ASSET = 16
        CUSTOMER_ASSET = 17
        CAMPAIGN_ASSET = 18
        AD_GROUP_ASSET = 19
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
