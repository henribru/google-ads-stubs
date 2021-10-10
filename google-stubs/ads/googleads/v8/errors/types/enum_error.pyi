from typing import Any

import proto

__protobuf__: Any

class EnumErrorEnum(proto.Message):
    class EnumError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENUM_VALUE_NOT_PERMITTED: int
