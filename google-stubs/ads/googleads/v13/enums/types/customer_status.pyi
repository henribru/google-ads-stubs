from typing import Any

import proto

class CustomerStatusEnum(proto.Message):
    class CustomerStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        CANCELED = 3
        SUSPENDED = 4
        CLOSED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
