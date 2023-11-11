from typing import Any

import proto

class ListingGroupFilterListingSourceEnum(proto.Message):
    class ListingGroupFilterListingSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SHOPPING = 2
        WEBPAGE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
