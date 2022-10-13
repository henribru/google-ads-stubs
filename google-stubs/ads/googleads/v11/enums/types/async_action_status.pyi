from typing import Any

import proto

class AsyncActionStatusEnum(proto.Message):
    class AsyncActionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_STARTED = 2
        IN_PROGRESS = 3
        COMPLETED = 4
        FAILED = 5
        COMPLETED_WITH_WARNING = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
