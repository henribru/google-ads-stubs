from typing import Any

import proto

class UserListCombinedRuleOperatorEnum(proto.Message):
    class UserListCombinedRuleOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AND = 2
        AND_NOT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
