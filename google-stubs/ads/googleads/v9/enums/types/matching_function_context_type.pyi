from typing import Any

import proto

__protobuf__: Any

class MatchingFunctionContextTypeEnum(proto.Message):
    class MatchingFunctionContextType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ITEM_ID: int
        DEVICE_NAME: int
        FEED_ITEM_SET_ID: int
