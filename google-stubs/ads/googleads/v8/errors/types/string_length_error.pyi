from typing import Any

import proto

__protobuf__: Any

class StringLengthErrorEnum(proto.Message):
    class StringLengthError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EMPTY: int
        TOO_SHORT: int
        TOO_LONG: int
