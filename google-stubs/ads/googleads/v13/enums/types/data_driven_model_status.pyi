from typing import Any

import proto

class DataDrivenModelStatusEnum(proto.Message):
    class DataDrivenModelStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AVAILABLE = 2
        STALE = 3
        EXPIRED = 4
        NEVER_GENERATED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
