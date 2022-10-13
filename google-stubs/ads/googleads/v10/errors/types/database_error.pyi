from typing import Any

import proto

class DatabaseErrorEnum(proto.Message):
    class DatabaseError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONCURRENT_MODIFICATION = 2
        DATA_CONSTRAINT_VIOLATION = 3
        REQUEST_TOO_LARGE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
