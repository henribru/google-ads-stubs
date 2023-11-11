from typing import Any

import proto

class LookalikeExpansionLevelEnum(proto.Message):
    class LookalikeExpansionLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NARROW = 2
        BALANCED = 3
        BROAD = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
