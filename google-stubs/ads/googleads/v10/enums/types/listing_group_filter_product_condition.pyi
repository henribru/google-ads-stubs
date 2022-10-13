from typing import Any

import proto

class ListingGroupFilterProductConditionEnum(proto.Message):
    class ListingGroupFilterProductCondition(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 2
        REFURBISHED = 3
        USED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
