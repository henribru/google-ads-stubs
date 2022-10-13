from typing import Any

import proto

class TimeTypeEnum(proto.Message):
    class TimeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOW = 2
        FOREVER = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
