from typing import Any

import proto

__protobuf__: Any

class UserListCombinedRuleOperatorEnum(proto.Message):
    class UserListCombinedRuleOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AND: int
        AND_NOT: int
