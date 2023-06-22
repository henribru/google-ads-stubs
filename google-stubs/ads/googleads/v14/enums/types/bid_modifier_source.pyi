from typing import Any

import proto

class BidModifierSourceEnum(proto.Message):
    class BidModifierSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN = 2
        AD_GROUP = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
