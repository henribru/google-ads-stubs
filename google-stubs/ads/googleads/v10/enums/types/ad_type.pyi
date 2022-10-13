from typing import Any

import proto

class AdTypeEnum(proto.Message):
    class AdType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT_AD = 2
        EXPANDED_TEXT_AD = 3
        EXPANDED_DYNAMIC_SEARCH_AD = 7
        HOTEL_AD = 8
        SHOPPING_SMART_AD = 9
        SHOPPING_PRODUCT_AD = 10
        VIDEO_AD = 12
        GMAIL_AD = 13
        IMAGE_AD = 14
        RESPONSIVE_SEARCH_AD = 15
        LEGACY_RESPONSIVE_DISPLAY_AD = 16
        APP_AD = 17
        LEGACY_APP_INSTALL_AD = 18
        RESPONSIVE_DISPLAY_AD = 19
        LOCAL_AD = 20
        HTML5_UPLOAD_AD = 21
        DYNAMIC_HTML5_AD = 22
        APP_ENGAGEMENT_AD = 23
        SHOPPING_COMPARISON_LISTING_AD = 24
        VIDEO_BUMPER_AD = 25
        VIDEO_NON_SKIPPABLE_IN_STREAM_AD = 26
        VIDEO_OUTSTREAM_AD = 27
        VIDEO_TRUEVIEW_IN_STREAM_AD = 29
        VIDEO_RESPONSIVE_AD = 30
        SMART_CAMPAIGN_AD = 31
        CALL_AD = 32
        APP_PRE_REGISTRATION_AD = 33
        IN_FEED_VIDEO_AD = 34
        DISCOVERY_MULTI_ASSET_AD = 35
        DISCOVERY_CAROUSEL_AD = 36
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
