from typing import Any

import proto

__protobuf__: Any

class RealEstatePlaceholderFieldEnum(proto.Message):
    class RealEstatePlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LISTING_ID: int
        LISTING_NAME: int
        CITY_NAME: int
        DESCRIPTION: int
        ADDRESS: int
        PRICE: int
        FORMATTED_PRICE: int
        IMAGE_URL: int
        PROPERTY_TYPE: int
        LISTING_TYPE: int
        CONTEXTUAL_KEYWORDS: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_LISTING_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
