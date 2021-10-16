from typing import Any

import proto

__protobuf__: Any

class NotAllowlistedErrorEnum(proto.Message):
    class NotAllowlistedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE: int
