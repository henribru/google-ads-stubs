from typing import Any

import proto

class ProductCategoryStateEnum(proto.Message):
    class ProductCategoryState(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        OBSOLETE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
