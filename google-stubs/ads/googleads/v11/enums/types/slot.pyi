from typing import Any

import proto

class SlotEnum(proto.Message):
    class Slot(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH_SIDE = 2
        SEARCH_TOP = 3
        SEARCH_OTHER = 4
        CONTENT = 5
        SEARCH_PARTNER_TOP = 6
        SEARCH_PARTNER_OTHER = 7
        MIXED = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
