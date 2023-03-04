from typing import Any

import proto

class ListingGroupTypeEnum(proto.Message):
    class ListingGroupType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SUBDIVISION = 2
        UNIT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
