from typing import Any

import proto

class FieldErrorEnum(proto.Message):
    class FieldError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUIRED = 2
        IMMUTABLE_FIELD = 3
        INVALID_VALUE = 4
        VALUE_MUST_BE_UNSET = 5
        REQUIRED_NONEMPTY_LIST = 6
        FIELD_CANNOT_BE_CLEARED = 7
        BLOCKED_VALUE = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
