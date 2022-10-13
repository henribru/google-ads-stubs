from typing import Any

import proto

class LocalPlaceholderFieldEnum(proto.Message):
    class LocalPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEAL_ID = 2
        DEAL_NAME = 3
        SUBTITLE = 4
        DESCRIPTION = 5
        PRICE = 6
        FORMATTED_PRICE = 7
        SALE_PRICE = 8
        FORMATTED_SALE_PRICE = 9
        IMAGE_URL = 10
        ADDRESS = 11
        CATEGORY = 12
        CONTEXTUAL_KEYWORDS = 13
        FINAL_URLS = 14
        FINAL_MOBILE_URLS = 15
        TRACKING_URL = 16
        ANDROID_APP_LINK = 17
        SIMILAR_DEAL_IDS = 18
        IOS_APP_LINK = 19
        IOS_APP_STORE_ID = 20
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
