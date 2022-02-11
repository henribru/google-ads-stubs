from typing import Any

import proto

__protobuf__: Any

class StringFormatErrorEnum(proto.Message):
    class StringFormatError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ILLEGAL_CHARS: int
        INVALID_FORMAT: int
