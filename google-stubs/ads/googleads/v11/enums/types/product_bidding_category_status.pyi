from typing import Any

import proto

class ProductBiddingCategoryStatusEnum(proto.Message):
    class ProductBiddingCategoryStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACTIVE = 2
        OBSOLETE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
