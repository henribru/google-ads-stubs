from typing import Any

import proto

__protobuf__: Any

class ChangeEventErrorEnum(proto.Message):
    class ChangeEventError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        START_DATE_TOO_OLD: int
        CHANGE_DATE_RANGE_INFINITE: int
        CHANGE_DATE_RANGE_NEGATIVE: int
        LIMIT_NOT_SPECIFIED: int
        INVALID_LIMIT_CLAUSE: int
