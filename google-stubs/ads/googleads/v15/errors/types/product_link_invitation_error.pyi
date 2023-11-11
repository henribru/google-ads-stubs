from typing import Any

import proto

class ProductLinkInvitationErrorEnum(proto.Message):
    class ProductLinkInvitationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_STATUS = 2
        PERMISSION_DENIED = 3
        NO_INVITATION_REQUIRED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
