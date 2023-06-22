from typing import Any

import proto

class TravelPlaceholderFieldEnum(proto.Message):
    class TravelPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DESTINATION_ID = 2
        ORIGIN_ID = 3
        TITLE = 4
        DESTINATION_NAME = 5
        ORIGIN_NAME = 6
        PRICE = 7
        FORMATTED_PRICE = 8
        SALE_PRICE = 9
        FORMATTED_SALE_PRICE = 10
        IMAGE_URL = 11
        CATEGORY = 12
        CONTEXTUAL_KEYWORDS = 13
        DESTINATION_ADDRESS = 14
        FINAL_URL = 15
        FINAL_MOBILE_URLS = 16
        TRACKING_URL = 17
        ANDROID_APP_LINK = 18
        SIMILAR_DESTINATION_IDS = 19
        IOS_APP_LINK = 20
        IOS_APP_STORE_ID = 21
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
