from typing import Any

import proto

class OfflineUserDataJobStatusEnum(proto.Message):
    class OfflineUserDataJobStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        RUNNING = 3
        SUCCESS = 4
        FAILED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
