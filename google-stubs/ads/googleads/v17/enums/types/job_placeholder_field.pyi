from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class JobPlaceholderFieldEnum(proto.Message):
    class JobPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        JOB_ID = 2
        LOCATION_ID = 3
        TITLE = 4
        SUBTITLE = 5
        DESCRIPTION = 6
        IMAGE_URL = 7
        CATEGORY = 8
        CONTEXTUAL_KEYWORDS = 9
        ADDRESS = 10
        SALARY = 11
        FINAL_URLS = 12
        FINAL_MOBILE_URLS = 14
        TRACKING_URL = 15
        ANDROID_APP_LINK = 16
        SIMILAR_JOB_IDS = 17
        IOS_APP_LINK = 18
        IOS_APP_STORE_ID = 19

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
