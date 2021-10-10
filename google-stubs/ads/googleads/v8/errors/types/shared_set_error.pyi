from typing import Any

import proto

__protobuf__: Any

class SharedSetErrorEnum(proto.Message):
    class SharedSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE: int
        DUPLICATE_NAME: int
        SHARED_SET_REMOVED: int
        SHARED_SET_IN_USE: int
