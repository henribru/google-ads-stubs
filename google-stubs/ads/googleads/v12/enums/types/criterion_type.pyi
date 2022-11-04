from typing import Any

import proto

class CriterionTypeEnum(proto.Message):
    class CriterionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD = 2
        PLACEMENT = 3
        MOBILE_APP_CATEGORY = 4
        MOBILE_APPLICATION = 5
        DEVICE = 6
        LOCATION = 7
        LISTING_GROUP = 8
        AD_SCHEDULE = 9
        AGE_RANGE = 10
        GENDER = 11
        INCOME_RANGE = 12
        PARENTAL_STATUS = 13
        YOUTUBE_VIDEO = 14
        YOUTUBE_CHANNEL = 15
        USER_LIST = 16
        PROXIMITY = 17
        TOPIC = 18
        LISTING_SCOPE = 19
        LANGUAGE = 20
        IP_BLOCK = 21
        CONTENT_LABEL = 22
        CARRIER = 23
        USER_INTEREST = 24
        WEBPAGE = 25
        OPERATING_SYSTEM_VERSION = 26
        APP_PAYMENT_MODEL = 27
        MOBILE_DEVICE = 28
        CUSTOM_AFFINITY = 29
        CUSTOM_INTENT = 30
        LOCATION_GROUP = 31
        CUSTOM_AUDIENCE = 32
        COMBINED_AUDIENCE = 33
        KEYWORD_THEME = 34
        AUDIENCE = 35
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
