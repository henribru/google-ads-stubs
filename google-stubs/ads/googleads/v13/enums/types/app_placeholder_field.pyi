from typing import Any

import proto

class AppPlaceholderFieldEnum(proto.Message):
    class AppPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STORE = 2
        ID = 3
        LINK_TEXT = 4
        URL = 5
        FINAL_URLS = 6
        FINAL_MOBILE_URLS = 7
        TRACKING_URL = 8
        FINAL_URL_SUFFIX = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
