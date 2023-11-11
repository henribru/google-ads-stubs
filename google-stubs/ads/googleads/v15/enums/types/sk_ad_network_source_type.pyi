from typing import Any

import proto

class SkAdNetworkSourceTypeEnum(proto.Message):
    class SkAdNetworkSourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        WEBSITE = 3
        MOBILE_APPLICATION = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
