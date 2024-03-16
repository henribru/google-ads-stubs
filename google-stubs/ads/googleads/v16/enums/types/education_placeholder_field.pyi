from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
