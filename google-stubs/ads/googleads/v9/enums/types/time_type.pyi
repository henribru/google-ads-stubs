from typing import Any

import proto

__protobuf__: Any

class TimeTypeEnum(proto.Message):
    class TimeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOW: int
        FOREVER: int
