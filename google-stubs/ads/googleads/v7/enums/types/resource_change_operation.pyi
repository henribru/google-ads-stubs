from typing import Any

import proto

__protobuf__: Any

class ResourceChangeOperationEnum(proto.Message):
    class ResourceChangeOperation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREATE: int
        UPDATE: int
        REMOVE: int
