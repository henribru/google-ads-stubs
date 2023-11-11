from typing import Any

import proto

class UserListNumberRuleItemOperatorEnum(proto.Message):
    class UserListNumberRuleItemOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GREATER_THAN = 2
        GREATER_THAN_OR_EQUAL = 3
        EQUALS = 4
        NOT_EQUALS = 5
        LESS_THAN = 6
        LESS_THAN_OR_EQUAL = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
