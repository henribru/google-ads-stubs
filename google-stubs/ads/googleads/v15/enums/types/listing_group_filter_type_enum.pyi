from typing import Any

import proto

class ListingGroupFilterTypeEnum(proto.Message):
    class ListingGroupFilterType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SUBDIVISION = 2
        UNIT_INCLUDED = 3
        UNIT_EXCLUDED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
