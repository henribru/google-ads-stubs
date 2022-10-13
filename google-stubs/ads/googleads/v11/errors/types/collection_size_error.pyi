from typing import Any

import proto

class CollectionSizeErrorEnum(proto.Message):
    class CollectionSizeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_FEW = 2
        TOO_MANY = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
