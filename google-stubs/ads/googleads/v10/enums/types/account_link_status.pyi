from typing import Any

import proto

class AccountLinkStatusEnum(proto.Message):
    class AccountLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        REMOVED = 3
        REQUESTED = 4
        PENDING_APPROVAL = 5
        REJECTED = 6
        REVOKED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
