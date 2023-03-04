from typing import Any

import proto

class UserListLogicalRuleOperatorEnum(proto.Message):
    class UserListLogicalRuleOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL = 2
        ANY = 3
        NONE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
