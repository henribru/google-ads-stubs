from typing import Any

import proto

class IdErrorEnum(proto.Message):
    class IdError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_FOUND = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
