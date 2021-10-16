from typing import Any

import proto

__protobuf__: Any

class CustomerErrorEnum(proto.Message):
    class CustomerError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STATUS_CHANGE_DISALLOWED: int
        ACCOUNT_NOT_SET_UP: int
