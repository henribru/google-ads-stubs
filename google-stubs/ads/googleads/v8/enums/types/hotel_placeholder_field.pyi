from typing import Any

import proto

__protobuf__: Any

class HotelPlaceholderFieldEnum(proto.Message):
    class HotelPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROPERTY_ID: int
        PROPERTY_NAME: int
        DESTINATION_NAME: int
        DESCRIPTION: int
        ADDRESS: int
        PRICE: int
        FORMATTED_PRICE: int
        SALE_PRICE: int
        FORMATTED_SALE_PRICE: int
        IMAGE_URL: int
        CATEGORY: int
        STAR_RATING: int
        CONTEXTUAL_KEYWORDS: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_PROPERTY_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
