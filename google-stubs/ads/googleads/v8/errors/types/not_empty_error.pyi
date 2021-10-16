from typing import Any

import proto

__protobuf__: Any

class NotEmptyErrorEnum(proto.Message):
    class NotEmptyError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EMPTY_LIST: int
