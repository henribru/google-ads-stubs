from typing import Any

import proto

__protobuf__: Any

class AppPlaceholderFieldEnum(proto.Message):
    class AppPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STORE: int
        ID: int
        LINK_TEXT: int
        URL: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        FINAL_URL_SUFFIX: int
