from typing import Any

import proto

__protobuf__: Any

class TimeZoneErrorEnum(proto.Message):
    class TimeZoneError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_TIME_ZONE: int
