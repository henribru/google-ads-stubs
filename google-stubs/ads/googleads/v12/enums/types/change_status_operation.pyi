from typing import Any

import proto

class ChangeStatusOperationEnum(proto.Message):
    class ChangeStatusOperation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADDED = 2
        CHANGED = 3
        REMOVED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
