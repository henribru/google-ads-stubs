from typing import Any

import proto

__protobuf__: Any

class EducationPlaceholderFieldEnum(proto.Message):
    class EducationPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROGRAM_ID: int
        LOCATION_ID: int
        PROGRAM_NAME: int
        AREA_OF_STUDY: int
        PROGRAM_DESCRIPTION: int
        SCHOOL_NAME: int
        ADDRESS: int
        THUMBNAIL_IMAGE_URL: int
        ALTERNATIVE_THUMBNAIL_IMAGE_URL: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        CONTEXTUAL_KEYWORDS: int
        ANDROID_APP_LINK: int
        SIMILAR_PROGRAM_IDS: int
        IOS_APP_LINK: int
        IOS_APP_STORE_ID: int
