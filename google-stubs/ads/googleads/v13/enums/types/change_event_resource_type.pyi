from typing import Any

import proto

class ChangeEventResourceTypeEnum(proto.Message):
    class ChangeEventResourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD = 2
        AD_GROUP = 3
        AD_GROUP_CRITERION = 4
        CAMPAIGN = 5
        CAMPAIGN_BUDGET = 6
        AD_GROUP_BID_MODIFIER = 7
        CAMPAIGN_CRITERION = 8
        FEED = 9
        FEED_ITEM = 10
        CAMPAIGN_FEED = 11
        AD_GROUP_FEED = 12
        AD_GROUP_AD = 13
        ASSET = 14
        CUSTOMER_ASSET = 15
        CAMPAIGN_ASSET = 16
        AD_GROUP_ASSET = 17
        ASSET_SET = 18
        ASSET_SET_ASSET = 19
        CAMPAIGN_ASSET_SET = 20
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
