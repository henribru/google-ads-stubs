from typing import Any

import proto

class LocationStringFilterTypeEnum(proto.Message):
    class LocationStringFilterType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXACT = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
