from typing import Any

import proto

__protobuf__: Any

class CriterionTypeEnum(proto.Message):
    class CriterionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        KEYWORD: int
        PLACEMENT: int
        MOBILE_APP_CATEGORY: int
        MOBILE_APPLICATION: int
        DEVICE: int
        LOCATION: int
        LISTING_GROUP: int
        AD_SCHEDULE: int
        AGE_RANGE: int
        GENDER: int
        INCOME_RANGE: int
        PARENTAL_STATUS: int
        YOUTUBE_VIDEO: int
        YOUTUBE_CHANNEL: int
        USER_LIST: int
        PROXIMITY: int
        TOPIC: int
        LISTING_SCOPE: int
        LANGUAGE: int
        IP_BLOCK: int
        CONTENT_LABEL: int
        CARRIER: int
        USER_INTEREST: int
        WEBPAGE: int
        OPERATING_SYSTEM_VERSION: int
        APP_PAYMENT_MODEL: int
        MOBILE_DEVICE: int
        CUSTOM_AFFINITY: int
        CUSTOM_INTENT: int
        LOCATION_GROUP: int
        CUSTOM_AUDIENCE: int
        COMBINED_AUDIENCE: int
