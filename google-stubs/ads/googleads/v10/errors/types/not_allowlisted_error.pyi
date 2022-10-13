from typing import Any

import proto

class NotAllowlistedErrorEnum(proto.Message):
    class NotAllowlistedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
