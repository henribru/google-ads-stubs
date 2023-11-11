from typing import Any

import proto

class ProductLinkInvitationStatusEnum(proto.Message):
    class ProductLinkInvitationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCEPTED = 2
        REQUESTED = 3
        PENDING_APPROVAL = 4
        REVOKED = 5
        REJECTED = 6
        EXPIRED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
