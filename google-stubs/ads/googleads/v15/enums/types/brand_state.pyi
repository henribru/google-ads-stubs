from typing import Any

import proto

class BrandStateEnum(proto.Message):
    class BrandState(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        DEPRECATED = 3
        UNVERIFIED = 4
        APPROVED = 5
        CANCELLED = 6
        REJECTED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
