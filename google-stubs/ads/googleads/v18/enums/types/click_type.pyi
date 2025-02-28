from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ClickTypeEnum(proto.Message):
    class ClickType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APP_DEEPLINK = 2
        BREADCRUMBS = 3
        BROADBAND_PLAN = 4
        CALL_TRACKING = 5
        CALLS = 6
        CLICK_ON_ENGAGEMENT_AD = 7
        GET_DIRECTIONS = 8
        LOCATION_EXPANSION = 9
        LOCATION_FORMAT_CALL = 10
        LOCATION_FORMAT_DIRECTIONS = 11
        LOCATION_FORMAT_IMAGE = 12
        LOCATION_FORMAT_LANDING_PAGE = 13
        LOCATION_FORMAT_MAP = 14
        LOCATION_FORMAT_STORE_INFO = 15
        LOCATION_FORMAT_TEXT = 16
        MOBILE_CALL_TRACKING = 17
        OFFER_PRINTS = 18
        OTHER = 19
        PRODUCT_EXTENSION_CLICKS = 20
        PRODUCT_LISTING_AD_CLICKS = 21
        SITELINKS = 22
        STORE_LOCATOR = 23
        URL_CLICKS = 25
        VIDEO_APP_STORE_CLICKS = 26
        VIDEO_CALL_TO_ACTION_CLICKS = 27
        VIDEO_CARD_ACTION_HEADLINE_CLICKS = 28
        VIDEO_END_CAP_CLICKS = 29
        VIDEO_WEBSITE_CLICKS = 30
        VISUAL_SITELINKS = 31
        WIRELESS_PLAN = 32
        PRODUCT_LISTING_AD_LOCAL = 33
        PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL = 34
        PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE = 35
        PRODUCT_LISTING_ADS_COUPON = 36
        PRODUCT_LISTING_AD_TRANSACTABLE = 37
        PRODUCT_AD_APP_DEEPLINK = 38
        SHOWCASE_AD_CATEGORY_LINK = 39
        SHOWCASE_AD_LOCAL_STOREFRONT_LINK = 40
        SHOWCASE_AD_ONLINE_PRODUCT_LINK = 42
        SHOWCASE_AD_LOCAL_PRODUCT_LINK = 43
        PROMOTION_EXTENSION = 44
        SWIPEABLE_GALLERY_AD_HEADLINE = 45
        SWIPEABLE_GALLERY_AD_SWIPES = 46
        SWIPEABLE_GALLERY_AD_SEE_MORE = 47
        SWIPEABLE_GALLERY_AD_SITELINK_ONE = 48
        SWIPEABLE_GALLERY_AD_SITELINK_TWO = 49
        SWIPEABLE_GALLERY_AD_SITELINK_THREE = 50
        SWIPEABLE_GALLERY_AD_SITELINK_FOUR = 51
        SWIPEABLE_GALLERY_AD_SITELINK_FIVE = 52
        HOTEL_PRICE = 53
        PRICE_EXTENSION = 54
        HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION = 55
        SHOPPING_COMPARISON_LISTING = 56
        CROSS_NETWORK = 57
        AD_IMAGE = 58
        TRAVEL_ASSETS = 59

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
