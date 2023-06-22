from typing import Any

import proto

class ProductTypeLevelEnum(proto.Message):
    class ProductTypeLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LEVEL1 = 7
        LEVEL2 = 8
        LEVEL3 = 9
        LEVEL4 = 10
        LEVEL5 = 11
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
