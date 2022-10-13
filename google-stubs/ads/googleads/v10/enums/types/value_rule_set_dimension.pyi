from typing import Any

import proto

class ValueRuleSetDimensionEnum(proto.Message):
    class ValueRuleSetDimension(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GEO_LOCATION = 2
        DEVICE = 3
        AUDIENCE = 4
        NO_CONDITION = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
