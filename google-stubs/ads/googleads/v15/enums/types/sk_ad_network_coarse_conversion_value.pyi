from typing import Any

import proto

class SkAdNetworkCoarseConversionValueEnum(proto.Message):
    class SkAdNetworkCoarseConversionValue(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        LOW = 3
        MEDIUM = 4
        HIGH = 5
        NONE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
