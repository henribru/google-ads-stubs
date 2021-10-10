from typing import Any

import proto

__protobuf__: Any

class AdGroupTypeEnum(proto.Message):
    class AdGroupType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH_STANDARD: int
        DISPLAY_STANDARD: int
        SHOPPING_PRODUCT_ADS: int
        HOTEL_ADS: int
        SHOPPING_SMART_ADS: int
        VIDEO_BUMPER: int
        VIDEO_TRUE_VIEW_IN_STREAM: int
        VIDEO_TRUE_VIEW_IN_DISPLAY: int
        VIDEO_NON_SKIPPABLE_IN_STREAM: int
        VIDEO_OUTSTREAM: int
        SEARCH_DYNAMIC_ADS: int
        SHOPPING_COMPARISON_LISTING_ADS: int
        PROMOTED_HOTEL_ADS: int
        VIDEO_RESPONSIVE: int
        VIDEO_EFFICIENT_REACH: int
