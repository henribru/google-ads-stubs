from typing import Any

import proto

class PriceExtensionPriceUnitEnum(proto.Message):
    class PriceExtensionPriceUnit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PER_HOUR = 2
        PER_DAY = 3
        PER_WEEK = 4
        PER_MONTH = 5
        PER_YEAR = 6
        PER_NIGHT = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
