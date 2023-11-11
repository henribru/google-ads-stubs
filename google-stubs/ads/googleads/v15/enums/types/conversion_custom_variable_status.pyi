from typing import Any

import proto

class ConversionCustomVariableStatusEnum(proto.Message):
    class ConversionCustomVariableStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACTIVATION_NEEDED = 2
        ENABLED = 3
        PAUSED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
