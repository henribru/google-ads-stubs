from typing import Any

import proto

class HotelRateTypeEnum(proto.Message):
    class HotelRateType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        PUBLIC_RATE = 3
        QUALIFIED_RATE = 4
        PRIVATE_RATE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
