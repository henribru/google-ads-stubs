from typing import Any

import proto

class AdvertisingChannelSubTypeEnum(proto.Message):
    class AdvertisingChannelSubType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH_MOBILE_APP = 2
        DISPLAY_MOBILE_APP = 3
        SEARCH_EXPRESS = 4
        DISPLAY_EXPRESS = 5
        SHOPPING_SMART_ADS = 6
        DISPLAY_GMAIL_AD = 7
        DISPLAY_SMART_CAMPAIGN = 8
        VIDEO_OUTSTREAM = 9
        VIDEO_ACTION = 10
        VIDEO_NON_SKIPPABLE = 11
        APP_CAMPAIGN = 12
        APP_CAMPAIGN_FOR_ENGAGEMENT = 13
        LOCAL_CAMPAIGN = 14
        SHOPPING_COMPARISON_LISTING_ADS = 15
        SMART_CAMPAIGN = 16
        VIDEO_SEQUENCE = 17
        APP_CAMPAIGN_FOR_PRE_REGISTRATION = 18
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
