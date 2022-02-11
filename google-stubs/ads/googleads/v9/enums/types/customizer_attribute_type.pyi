from typing import Any

import proto

__protobuf__: Any

class CustomizerAttributeTypeEnum(proto.Message):
    class CustomizerAttributeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TEXT: int
        NUMBER: int
        PRICE: int
        PERCENT: int
