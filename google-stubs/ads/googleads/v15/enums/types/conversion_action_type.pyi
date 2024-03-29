from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ConversionActionTypeEnum(proto.Message):
    class ConversionActionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_CALL = 2
        CLICK_TO_CALL = 3
        GOOGLE_PLAY_DOWNLOAD = 4
        GOOGLE_PLAY_IN_APP_PURCHASE = 5
        UPLOAD_CALLS = 6
        UPLOAD_CLICKS = 7
        WEBPAGE = 8
        WEBSITE_CALL = 9
        STORE_SALES_DIRECT_UPLOAD = 10
        STORE_SALES = 11
        FIREBASE_ANDROID_FIRST_OPEN = 12
        FIREBASE_ANDROID_IN_APP_PURCHASE = 13
        FIREBASE_ANDROID_CUSTOM = 14
        FIREBASE_IOS_FIRST_OPEN = 15
        FIREBASE_IOS_IN_APP_PURCHASE = 16
        FIREBASE_IOS_CUSTOM = 17
        THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN = 18
        THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE = 19
        THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM = 20
        THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN = 21
        THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE = 22
        THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM = 23
        ANDROID_APP_PRE_REGISTRATION = 24
        ANDROID_INSTALLS_ALL_OTHER_APPS = 25
        FLOODLIGHT_ACTION = 26
        FLOODLIGHT_TRANSACTION = 27
        GOOGLE_HOSTED = 28
        LEAD_FORM_SUBMIT = 29
        SALESFORCE = 30
        SEARCH_ADS_360 = 31
        SMART_CAMPAIGN_AD_CLICKS_TO_CALL = 32
        SMART_CAMPAIGN_MAP_CLICKS_TO_CALL = 33
        SMART_CAMPAIGN_MAP_DIRECTIONS = 34
        SMART_CAMPAIGN_TRACKED_CALLS = 35
        STORE_VISITS = 36
        WEBPAGE_CODELESS = 37
        UNIVERSAL_ANALYTICS_GOAL = 38
        UNIVERSAL_ANALYTICS_TRANSACTION = 39
        GOOGLE_ANALYTICS_4_CUSTOM = 40
        GOOGLE_ANALYTICS_4_PURCHASE = 41

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
