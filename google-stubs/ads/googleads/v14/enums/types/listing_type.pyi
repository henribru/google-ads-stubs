from typing import Any

import proto

class ListingTypeEnum(proto.Message):
    class ListingType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VEHICLES = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
