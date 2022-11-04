from typing import Any

import proto

class ConversionAdjustmentTypeEnum(proto.Message):
    class ConversionAdjustmentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RETRACTION = 2
        RESTATEMENT = 3
        ENHANCEMENT = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
