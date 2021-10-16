from typing import Any

import proto

__protobuf__: Any

class UserListDateRuleItemOperatorEnum(proto.Message):
    class UserListDateRuleItemOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EQUALS: int
        NOT_EQUALS: int
        BEFORE: int
        AFTER: int
