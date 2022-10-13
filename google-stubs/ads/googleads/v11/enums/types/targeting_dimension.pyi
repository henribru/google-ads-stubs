from typing import Any

import proto

class TargetingDimensionEnum(proto.Message):
    class TargetingDimension(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD = 2
        AUDIENCE = 3
        TOPIC = 4
        GENDER = 5
        AGE_RANGE = 6
        PLACEMENT = 7
        PARENTAL_STATUS = 8
        INCOME_RANGE = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
