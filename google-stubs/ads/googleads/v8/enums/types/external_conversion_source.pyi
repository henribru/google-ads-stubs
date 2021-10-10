from typing import Any

import proto

__protobuf__: Any

class ExternalConversionSourceEnum(proto.Message):
    class ExternalConversionSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WEBPAGE: int
        ANALYTICS: int
        UPLOAD: int
        AD_CALL_METRICS: int
        WEBSITE_CALL_METRICS: int
        STORE_VISITS: int
        ANDROID_IN_APP: int
        IOS_IN_APP: int
        IOS_FIRST_OPEN: int
        APP_UNSPECIFIED: int
        ANDROID_FIRST_OPEN: int
        UPLOAD_CALLS: int
        FIREBASE: int
        CLICK_TO_CALL: int
        SALESFORCE: int
        STORE_SALES_CRM: int
        STORE_SALES_PAYMENT_NETWORK: int
        GOOGLE_PLAY: int
        THIRD_PARTY_APP_ANALYTICS: int
        GOOGLE_ATTRIBUTION: int
        STORE_SALES_DIRECT_UPLOAD: int
        STORE_SALES: int
        SEARCH_ADS_360: int
        GOOGLE_HOSTED: int
        FLOODLIGHT: int
        ANALYTICS_SEARCH_ADS_360: int
        FIREBASE_SEARCH_ADS_360: int
