from typing import Any

import proto

__protobuf__: Any

class IdErrorEnum(proto.Message):
    class IdError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_FOUND: int
