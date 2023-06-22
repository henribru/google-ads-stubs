from typing import Any

import proto

class TrackingCodeTypeEnum(proto.Message):
    class TrackingCodeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBPAGE = 2
        WEBPAGE_ONCLICK = 3
        CLICK_TO_CALL = 4
        WEBSITE_CALL = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
