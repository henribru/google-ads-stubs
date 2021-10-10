from typing import Any

import proto

__protobuf__: Any

class SitelinkPlaceholderFieldEnum(proto.Message):
    class SitelinkPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TEXT: int
        LINE_1: int
        LINE_2: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        FINAL_URL_SUFFIX: int
