from typing import Any

import proto

class ManagerLinkStatusEnum(proto.Message):
    class ManagerLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACTIVE = 2
        INACTIVE = 3
        PENDING = 4
        REFUSED = 5
        CANCELED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
