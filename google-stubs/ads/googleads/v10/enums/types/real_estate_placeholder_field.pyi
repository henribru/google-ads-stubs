from typing import Any

import proto

class RealEstatePlaceholderFieldEnum(proto.Message):
    class RealEstatePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LISTING_ID = 2
        LISTING_NAME = 3
        CITY_NAME = 4
        DESCRIPTION = 5
        ADDRESS = 6
        PRICE = 7
        FORMATTED_PRICE = 8
        IMAGE_URL = 9
        PROPERTY_TYPE = 10
        LISTING_TYPE = 11
        CONTEXTUAL_KEYWORDS = 12
        FINAL_URLS = 13
        FINAL_MOBILE_URLS = 14
        TRACKING_URL = 15
        ANDROID_APP_LINK = 16
        SIMILAR_LISTING_IDS = 17
        IOS_APP_LINK = 18
        IOS_APP_STORE_ID = 19
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
