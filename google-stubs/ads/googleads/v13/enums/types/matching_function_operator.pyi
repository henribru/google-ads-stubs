from typing import Any

import proto

class MatchingFunctionOperatorEnum(proto.Message):
    class MatchingFunctionOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IN = 2
        IDENTITY = 3
        EQUALS = 4
        AND = 5
        CONTAINS_ANY = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
