from typing import Any

import proto

class StringLengthErrorEnum(proto.Message):
    class StringLengthError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMPTY = 4
        TOO_SHORT = 2
        TOO_LONG = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
