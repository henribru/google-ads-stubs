from typing import Any

import proto

class ChangeEventErrorEnum(proto.Message):
    class ChangeEventError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        START_DATE_TOO_OLD = 2
        CHANGE_DATE_RANGE_INFINITE = 3
        CHANGE_DATE_RANGE_NEGATIVE = 4
        LIMIT_NOT_SPECIFIED = 5
        INVALID_LIMIT_CLAUSE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
