from typing import Any

import proto

class ProductChannelEnum(proto.Message):
    class ProductChannel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ONLINE = 2
        LOCAL = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
