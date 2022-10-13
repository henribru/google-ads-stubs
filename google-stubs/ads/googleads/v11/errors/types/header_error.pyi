from typing import Any

import proto

class HeaderErrorEnum(proto.Message):
    class HeaderError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_LOGIN_CUSTOMER_ID = 3
        INVALID_LINKED_CUSTOMER_ID = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
