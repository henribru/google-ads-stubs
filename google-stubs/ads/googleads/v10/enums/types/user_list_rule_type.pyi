from typing import Any

import proto

class UserListRuleTypeEnum(proto.Message):
    class UserListRuleType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AND_OF_ORS = 2
        OR_OF_ANDS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
