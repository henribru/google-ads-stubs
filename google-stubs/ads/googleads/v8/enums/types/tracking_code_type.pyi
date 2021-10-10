from typing import Any

import proto

__protobuf__: Any

class TrackingCodeTypeEnum(proto.Message):
    class TrackingCodeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WEBPAGE: int
        WEBPAGE_ONCLICK: int
        CLICK_TO_CALL: int
        WEBSITE_CALL: int
