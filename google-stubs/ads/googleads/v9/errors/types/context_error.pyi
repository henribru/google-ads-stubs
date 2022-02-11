from typing import Any

import proto

__protobuf__: Any

class ContextErrorEnum(proto.Message):
    class ContextError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPERATION_NOT_PERMITTED_FOR_CONTEXT: int
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: int
