from typing import Any

import proto

class ExternalConversionSourceEnum(proto.Message):
    class ExternalConversionSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBPAGE = 2
        ANALYTICS = 3
        UPLOAD = 4
        AD_CALL_METRICS = 5
        WEBSITE_CALL_METRICS = 6
        STORE_VISITS = 7
        ANDROID_IN_APP = 8
        IOS_IN_APP = 9
        IOS_FIRST_OPEN = 10
        APP_UNSPECIFIED = 11
        ANDROID_FIRST_OPEN = 12
        UPLOAD_CALLS = 13
        FIREBASE = 14
        CLICK_TO_CALL = 15
        SALESFORCE = 16
        STORE_SALES_CRM = 17
        STORE_SALES_PAYMENT_NETWORK = 18
        GOOGLE_PLAY = 19
        THIRD_PARTY_APP_ANALYTICS = 20
        GOOGLE_ATTRIBUTION = 21
        STORE_SALES_DIRECT_UPLOAD = 23
        STORE_SALES = 24
        SEARCH_ADS_360 = 25
        GOOGLE_HOSTED = 27
        FLOODLIGHT = 29
        ANALYTICS_SEARCH_ADS_360 = 31
        FIREBASE_SEARCH_ADS_360 = 33
        DISPLAY_AND_VIDEO_360_FLOODLIGHT = 34
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
