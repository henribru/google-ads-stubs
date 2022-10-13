from typing import Any

import proto

class SharedSetErrorEnum(proto.Message):
    class SharedSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE = 2
        DUPLICATE_NAME = 3
        SHARED_SET_REMOVED = 4
        SHARED_SET_IN_USE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
