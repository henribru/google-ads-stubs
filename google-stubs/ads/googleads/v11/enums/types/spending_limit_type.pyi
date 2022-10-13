from typing import Any

import proto

class SpendingLimitTypeEnum(proto.Message):
    class SpendingLimitType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INFINITE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
