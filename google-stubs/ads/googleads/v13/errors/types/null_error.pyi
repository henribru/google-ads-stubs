from typing import Any

import proto

class NullErrorEnum(proto.Message):
    class NullError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NULL_CONTENT = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
