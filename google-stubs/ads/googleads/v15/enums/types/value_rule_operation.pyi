from typing import Any

import proto

class ValueRuleOperationEnum(proto.Message):
    class ValueRuleOperation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
        MULTIPLY = 3
        SET = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
