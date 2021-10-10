from typing import Any

import proto

__protobuf__: Any

class ChangeStatusOperationEnum(proto.Message):
    class ChangeStatusOperation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADDED: int
        CHANGED: int
        REMOVED: int
