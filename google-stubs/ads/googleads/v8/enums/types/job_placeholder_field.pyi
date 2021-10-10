from typing import Any

import proto

__protobuf__: Any

class JobPlaceholderFieldEnum(proto.Message):
    class JobPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        JOB_ID: int
        LOCATION_ID: int
        TITLE: int
        SUBTITLE: int
        DESCRIPTION: int
        IMAGE_URL: int
        CATEGORY: int
        CONTEXTUAL_KEYWORDS: int
        ADDRESS: int
        SALARY: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        ANDROID_APP_LINK: int
        SIMILAR_JOB_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
