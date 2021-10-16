from typing import Any

import proto

__protobuf__: Any

class TravelPlaceholderFieldEnum(proto.Message):
    class TravelPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DESTINATION_ID: int
        ORIGIN_ID: int
        TITLE: int
        DESTINATION_NAME: int
        ORIGIN_NAME: int
        PRICE: int
        FORMATTED_PRICE: int
        SALE_PRICE: int
        FORMATTED_SALE_PRICE: int
        IMAGE_URL: int
        CATEGORY: int
        CONTEXTUAL_KEYWORDS: int
        DESTINATION_ADDRESS: int
        FINAL_URL: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_DESTINATION_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
