from typing import Any

import proto

class CustomAudienceTypeEnum(proto.Message):
    class CustomAudienceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AUTO = 2
        INTEREST = 3
        PURCHASE_INTENT = 4
        SEARCH = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
