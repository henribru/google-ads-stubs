from typing import Any

import proto

class AdGroupTypeEnum(proto.Message):
    class AdGroupType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH_STANDARD = 2
        DISPLAY_STANDARD = 3
        SHOPPING_PRODUCT_ADS = 4
        HOTEL_ADS = 6
        SHOPPING_SMART_ADS = 7
        VIDEO_BUMPER = 8
        VIDEO_TRUE_VIEW_IN_STREAM = 9
        VIDEO_TRUE_VIEW_IN_DISPLAY = 10
        VIDEO_NON_SKIPPABLE_IN_STREAM = 11
        VIDEO_OUTSTREAM = 12
        SEARCH_DYNAMIC_ADS = 13
        SHOPPING_COMPARISON_LISTING_ADS = 14
        PROMOTED_HOTEL_ADS = 15
        VIDEO_RESPONSIVE = 16
        VIDEO_EFFICIENT_REACH = 17
        SMART_CAMPAIGN_ADS = 18
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
