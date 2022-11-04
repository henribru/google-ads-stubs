from typing import Any

import proto

class KeywordPlanAdGroupErrorEnum(proto.Message):
    class KeywordPlanAdGroupError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_NAME = 2
        DUPLICATE_NAME = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
