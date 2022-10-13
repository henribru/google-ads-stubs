from typing import Any

import proto

class SkAdNetworkAdEventTypeEnum(proto.Message):
    class SkAdNetworkAdEventType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        INTERACTION = 3
        VIEW = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
