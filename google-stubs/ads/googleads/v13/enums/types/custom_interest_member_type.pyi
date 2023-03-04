from typing import Any

import proto

class CustomInterestMemberTypeEnum(proto.Message):
    class CustomInterestMemberType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD = 2
        URL = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
