from typing import Any

import proto

class AccessInvitationStatusEnum(proto.Message):
    class AccessInvitationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        DECLINED = 3
        EXPIRED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
