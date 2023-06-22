from typing import Any

import proto

class TimeZoneErrorEnum(proto.Message):
    class TimeZoneError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_TIME_ZONE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
