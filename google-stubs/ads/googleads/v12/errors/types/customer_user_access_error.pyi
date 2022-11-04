from typing import Any

import proto

class CustomerUserAccessErrorEnum(proto.Message):
    class CustomerUserAccessError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_USER_ID = 2
        REMOVAL_DISALLOWED = 3
        DISALLOWED_ACCESS_ROLE = 4
        LAST_ADMIN_USER_OF_SERVING_CUSTOMER = 5
        LAST_ADMIN_USER_OF_MANAGER = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
