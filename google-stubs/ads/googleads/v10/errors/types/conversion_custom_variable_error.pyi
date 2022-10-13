from typing import Any

import proto

class ConversionCustomVariableErrorEnum(proto.Message):
    class ConversionCustomVariableError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        DUPLICATE_TAG = 3
        RESERVED_TAG = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
