from typing import Any

import proto

class ConversionActionCountingTypeEnum(proto.Message):
    class ConversionActionCountingType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ONE_PER_CLICK = 2
        MANY_PER_CLICK = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
