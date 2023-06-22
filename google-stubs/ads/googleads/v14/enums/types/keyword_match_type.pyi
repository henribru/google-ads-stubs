from typing import Any

import proto

class KeywordMatchTypeEnum(proto.Message):
    class KeywordMatchType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXACT = 2
        PHRASE = 3
        BROAD = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
