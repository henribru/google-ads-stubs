import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

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
