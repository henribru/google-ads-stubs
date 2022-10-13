from typing import Any

import proto

class ListOperationErrorEnum(proto.Message):
    class ListOperationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUIRED_FIELD_MISSING = 7
        DUPLICATE_VALUES = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
