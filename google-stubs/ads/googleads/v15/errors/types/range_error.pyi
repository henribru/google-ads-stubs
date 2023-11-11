from typing import Any

import proto

class RangeErrorEnum(proto.Message):
    class RangeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_LOW = 2
        TOO_HIGH = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
