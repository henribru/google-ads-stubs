from typing import Any

import proto

__protobuf__: Any

class RangeErrorEnum(proto.Message):
    class RangeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_LOW: int
        TOO_HIGH: int
