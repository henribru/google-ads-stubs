from typing import Any

import proto

class CustomPlaceholderFieldEnum(proto.Message):
    class CustomPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ID = 2
        ID2 = 3
        ITEM_TITLE = 4
        ITEM_SUBTITLE = 5
        ITEM_DESCRIPTION = 6
        ITEM_ADDRESS = 7
        PRICE = 8
        FORMATTED_PRICE = 9
        SALE_PRICE = 10
        FORMATTED_SALE_PRICE = 11
        IMAGE_URL = 12
        ITEM_CATEGORY = 13
        FINAL_URLS = 14
        FINAL_MOBILE_URLS = 15
        TRACKING_URL = 16
        CONTEXTUAL_KEYWORDS = 17
        ANDROID_APP_LINK = 18
        SIMILAR_IDS = 19
        IOS_APP_LINK = 20
        IOS_APP_STORE_ID = 21
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
