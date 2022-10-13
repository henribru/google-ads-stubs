from typing import Any

import proto

class ProductConditionEnum(proto.Message):
    class ProductCondition(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 3
        REFURBISHED = 4
        USED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
