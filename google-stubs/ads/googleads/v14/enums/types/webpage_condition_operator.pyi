from typing import Any

import proto

class WebpageConditionOperatorEnum(proto.Message):
    class WebpageConditionOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EQUALS = 2
        CONTAINS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
