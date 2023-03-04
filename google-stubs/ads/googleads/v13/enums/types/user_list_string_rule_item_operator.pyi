from typing import Any

import proto

class UserListStringRuleItemOperatorEnum(proto.Message):
    class UserListStringRuleItemOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONTAINS = 2
        EQUALS = 3
        STARTS_WITH = 4
        ENDS_WITH = 5
        NOT_EQUALS = 6
        NOT_CONTAINS = 7
        NOT_STARTS_WITH = 8
        NOT_ENDS_WITH = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
