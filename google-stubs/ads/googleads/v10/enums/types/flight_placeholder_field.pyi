from typing import Any

import proto

class FlightPlaceholderFieldEnum(proto.Message):
    class FlightPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DESTINATION_ID = 2
        ORIGIN_ID = 3
        FLIGHT_DESCRIPTION = 4
        ORIGIN_NAME = 5
        DESTINATION_NAME = 6
        FLIGHT_PRICE = 7
        FORMATTED_PRICE = 8
        FLIGHT_SALE_PRICE = 9
        FORMATTED_SALE_PRICE = 10
        IMAGE_URL = 11
        FINAL_URLS = 12
        FINAL_MOBILE_URLS = 13
        TRACKING_URL = 14
        ANDROID_APP_LINK = 15
        SIMILAR_DESTINATION_IDS = 16
        IOS_APP_LINK = 17
        IOS_APP_STORE_ID = 18
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
