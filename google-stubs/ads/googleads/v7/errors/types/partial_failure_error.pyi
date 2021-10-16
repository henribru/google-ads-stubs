from typing import Any

import proto

__protobuf__: Any

class PartialFailureErrorEnum(proto.Message):
    class PartialFailureError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PARTIAL_FAILURE_MODE_REQUIRED: int
