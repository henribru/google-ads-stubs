from typing import Any

import proto

class HotelPriceBucketEnum(proto.Message):
    class HotelPriceBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOWEST_UNIQUE = 2
        LOWEST_TIED = 3
        NOT_LOWEST = 4
        ONLY_PARTNER_SHOWN = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
