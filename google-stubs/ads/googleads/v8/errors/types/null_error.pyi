from typing import Any

import proto

__protobuf__: Any

class NullErrorEnum(proto.Message):
    class NullError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NULL_CONTENT: int
