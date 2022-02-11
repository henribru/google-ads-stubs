from typing import Any

import proto

__protobuf__: Any

class ListOperationErrorEnum(proto.Message):
    class ListOperationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUIRED_FIELD_MISSING: int
        DUPLICATE_VALUES: int
