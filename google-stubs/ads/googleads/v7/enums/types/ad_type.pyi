from typing import Any

import proto

__protobuf__: Any

class AdTypeEnum(proto.Message):
    class AdType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TEXT_AD: int
        EXPANDED_TEXT_AD: int
        CALL_ONLY_AD: int
        EXPANDED_DYNAMIC_SEARCH_AD: int
        HOTEL_AD: int
        SHOPPING_SMART_AD: int
        SHOPPING_PRODUCT_AD: int
        VIDEO_AD: int
        GMAIL_AD: int
        IMAGE_AD: int
        RESPONSIVE_SEARCH_AD: int
        LEGACY_RESPONSIVE_DISPLAY_AD: int
        APP_AD: int
        LEGACY_APP_INSTALL_AD: int
        RESPONSIVE_DISPLAY_AD: int
        LOCAL_AD: int
        HTML5_UPLOAD_AD: int
        DYNAMIC_HTML5_AD: int
        APP_ENGAGEMENT_AD: int
        SHOPPING_COMPARISON_LISTING_AD: int
        VIDEO_BUMPER_AD: int
        VIDEO_NON_SKIPPABLE_IN_STREAM_AD: int
        VIDEO_OUTSTREAM_AD: int
        VIDEO_TRUEVIEW_DISCOVERY_AD: int
        VIDEO_TRUEVIEW_IN_STREAM_AD: int
        VIDEO_RESPONSIVE_AD: int
