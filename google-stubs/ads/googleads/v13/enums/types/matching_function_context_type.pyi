from typing import Any

import proto

class MatchingFunctionContextTypeEnum(proto.Message):
    class MatchingFunctionContextType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ITEM_ID = 2
        DEVICE_NAME = 3
        FEED_ITEM_SET_ID = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
