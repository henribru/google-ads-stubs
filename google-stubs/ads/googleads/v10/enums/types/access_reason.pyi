from typing import Any

import proto

class AccessReasonEnum(proto.Message):
    class AccessReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OWNED = 2
        SHARED = 3
        LICENSED = 4
        SUBSCRIBED = 5
        AFFILIATED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
