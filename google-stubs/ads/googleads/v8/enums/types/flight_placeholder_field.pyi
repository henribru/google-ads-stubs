from typing import Any

import proto

__protobuf__: Any

class FlightPlaceholderFieldEnum(proto.Message):
    class FlightPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DESTINATION_ID: int
        ORIGIN_ID: int
        FLIGHT_DESCRIPTION: int
        ORIGIN_NAME: int
        DESTINATION_NAME: int
        FLIGHT_PRICE: int
        FORMATTED_PRICE: int
        FLIGHT_SALE_PRICE: int
        FORMATTED_SALE_PRICE: int
        IMAGE_URL: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_DESTINATION_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
