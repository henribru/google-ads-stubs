from typing import Any

import proto

class SearchTermMatchTypeEnum(proto.Message):
    class SearchTermMatchType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BROAD = 2
        EXACT = 3
        PHRASE = 4
        NEAR_EXACT = 5
        NEAR_PHRASE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
