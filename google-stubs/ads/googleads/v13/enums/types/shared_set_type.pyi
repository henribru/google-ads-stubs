from typing import Any

import proto

class SharedSetTypeEnum(proto.Message):
    class SharedSetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEGATIVE_KEYWORDS = 2
        NEGATIVE_PLACEMENTS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
