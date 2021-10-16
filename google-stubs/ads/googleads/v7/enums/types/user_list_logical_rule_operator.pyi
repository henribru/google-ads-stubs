from typing import Any

import proto

__protobuf__: Any

class UserListLogicalRuleOperatorEnum(proto.Message):
    class UserListLogicalRuleOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ALL: int
        ANY: int
        NONE: int
