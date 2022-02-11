from typing import Any

import proto

__protobuf__: Any

class ListingGroupFilterProductConditionEnum(proto.Message):
    class ListingGroupFilterProductCondition(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEW: int
        REFURBISHED: int
        USED: int
