from typing import Any

import proto

__protobuf__: Any

class FieldErrorEnum(proto.Message):
    class FieldError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUIRED: int
        IMMUTABLE_FIELD: int
        INVALID_VALUE: int
        VALUE_MUST_BE_UNSET: int
        REQUIRED_NONEMPTY_LIST: int
        FIELD_CANNOT_BE_CLEARED: int
        BLOCKED_VALUE: int
