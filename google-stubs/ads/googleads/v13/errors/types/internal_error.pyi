from typing import Any

import proto

class InternalErrorEnum(proto.Message):
    class InternalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INTERNAL_ERROR = 2
        ERROR_CODE_NOT_PUBLISHED = 3
        TRANSIENT_ERROR = 4
        DEADLINE_EXCEEDED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
