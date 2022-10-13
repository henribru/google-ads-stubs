from typing import Any

import proto

class CustomizerAttributeTypeEnum(proto.Message):
    class CustomizerAttributeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT = 2
        NUMBER = 3
        PRICE = 4
        PERCENT = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
