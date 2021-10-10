from typing import Any

import proto

__protobuf__: Any

class ResourceAccessDeniedErrorEnum(proto.Message):
    class ResourceAccessDeniedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WRITE_ACCESS_DENIED: int
