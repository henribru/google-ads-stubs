from typing import Any

import proto

class UserDataErrorEnum(proto.Message):
    class UserDataError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED = 2
        TOO_MANY_USER_IDENTIFIERS = 3
        USER_LIST_NOT_APPLICABLE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
