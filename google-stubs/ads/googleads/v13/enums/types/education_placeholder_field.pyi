from typing import Any

import proto

class EducationPlaceholderFieldEnum(proto.Message):
    class EducationPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROGRAM_ID = 2
        LOCATION_ID = 3
        PROGRAM_NAME = 4
        AREA_OF_STUDY = 5
        PROGRAM_DESCRIPTION = 6
        SCHOOL_NAME = 7
        ADDRESS = 8
        THUMBNAIL_IMAGE_URL = 9
        ALTERNATIVE_THUMBNAIL_IMAGE_URL = 10
        FINAL_URLS = 11
        FINAL_MOBILE_URLS = 12
        TRACKING_URL = 13
        CONTEXTUAL_KEYWORDS = 14
        ANDROID_APP_LINK = 15
        SIMILAR_PROGRAM_IDS = 16
        IOS_APP_LINK = 17
        IOS_APP_STORE_ID = 18
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
