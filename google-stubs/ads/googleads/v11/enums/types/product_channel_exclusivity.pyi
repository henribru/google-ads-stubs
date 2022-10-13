from typing import Any

import proto

class ProductChannelExclusivityEnum(proto.Message):
    class ProductChannelExclusivity(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SINGLE_CHANNEL = 2
        MULTI_CHANNEL = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
