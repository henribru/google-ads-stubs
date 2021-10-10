from typing import Any

import proto

__protobuf__: Any

class CustomPlaceholderFieldEnum(proto.Message):
    class CustomPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ID: int
        ID2: int
        ITEM_TITLE: int
        ITEM_SUBTITLE: int
        ITEM_DESCRIPTION: int
        ITEM_ADDRESS: int
        PRICE: int
        FORMATTED_PRICE: int
        SALE_PRICE: int
        FORMATTED_SALE_PRICE: int
        IMAGE_URL: int
        ITEM_CATEGORY: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        CONTEXTUAL_KEYWORDS: int
        ANDROID_APP_LINK: int
        SIMILAR_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
