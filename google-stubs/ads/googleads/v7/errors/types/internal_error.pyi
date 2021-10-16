from typing import Any

import proto

__protobuf__: Any

class InternalErrorEnum(proto.Message):
    class InternalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INTERNAL_ERROR: int
        ERROR_CODE_NOT_PUBLISHED: int
        TRANSIENT_ERROR: int
        DEADLINE_EXCEEDED: int
