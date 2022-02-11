from typing import Any

import proto

__protobuf__: Any

class AdvertisingChannelSubTypeEnum(proto.Message):
    class AdvertisingChannelSubType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH_MOBILE_APP: int
        DISPLAY_MOBILE_APP: int
        SEARCH_EXPRESS: int
        DISPLAY_EXPRESS: int
        SHOPPING_SMART_ADS: int
        DISPLAY_GMAIL_AD: int
        DISPLAY_SMART_CAMPAIGN: int
        VIDEO_OUTSTREAM: int
        VIDEO_ACTION: int
        VIDEO_NON_SKIPPABLE: int
        APP_CAMPAIGN: int
        APP_CAMPAIGN_FOR_ENGAGEMENT: int
        LOCAL_CAMPAIGN: int
        SHOPPING_COMPARISON_LISTING_ADS: int
        SMART_CAMPAIGN: int
        VIDEO_SEQUENCE: int
        APP_CAMPAIGN_FOR_PRE_REGISTRATION: int
