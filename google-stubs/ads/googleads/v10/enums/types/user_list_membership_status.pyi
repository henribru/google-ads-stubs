from typing import Any

import proto

class UserListMembershipStatusEnum(proto.Message):
    class UserListMembershipStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPEN = 2
        CLOSED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
