from typing import Any

import proto

class UserListFlexibleRuleOperatorEnum(proto.Message):
    class UserListFlexibleRuleOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AND = 2
        OR = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
