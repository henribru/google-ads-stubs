from typing import Any

import proto

class AccessRoleEnum(proto.Message):
    class AccessRole(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADMIN = 2
        STANDARD = 3
        READ_ONLY = 4
        EMAIL_ONLY = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
