from typing import Any

import proto

__protobuf__: Any

class ProductConditionEnum(proto.Message):
    class ProductCondition(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEW: int
        REFURBISHED: int
        USED: int
