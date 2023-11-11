from typing import Any

import proto

class ConversionValueRuleSetStatusEnum(proto.Message):
    class ConversionValueRuleSetStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        REMOVED = 3
        PAUSED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
