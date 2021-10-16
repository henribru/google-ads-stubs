from typing import Any

import proto

__protobuf__: Any

class LocalPlaceholderFieldEnum(proto.Message):
    class LocalPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DEAL_ID: int
        DEAL_NAME: int
        SUBTITLE: int
        DESCRIPTION: int
        PRICE: int
        FORMATTED_PRICE: int
        SALE_PRICE: int
        FORMATTED_SALE_PRICE: int
        IMAGE_URL: int
        ADDRESS: int
        CATEGORY: int
        CONTEXTUAL_KEYWORDS: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_DEAL_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
