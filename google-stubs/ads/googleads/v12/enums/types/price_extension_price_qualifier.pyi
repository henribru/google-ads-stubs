from typing import Any

import proto

class PriceExtensionPriceQualifierEnum(proto.Message):
    class PriceExtensionPriceQualifier(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FROM = 2
        UP_TO = 3
        AVERAGE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
