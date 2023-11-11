from typing import Any

import proto

class LocationSourceTypeEnum(proto.Message):
    class LocationSourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOOGLE_MY_BUSINESS = 2
        AFFILIATE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
