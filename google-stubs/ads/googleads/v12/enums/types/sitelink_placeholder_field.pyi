from typing import Any

import proto

class SitelinkPlaceholderFieldEnum(proto.Message):
    class SitelinkPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT = 2
        LINE_1 = 3
        LINE_2 = 4
        FINAL_URLS = 5
        FINAL_MOBILE_URLS = 6
        TRACKING_URL = 7
        FINAL_URL_SUFFIX = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
