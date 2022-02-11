from typing import Any

import proto

__protobuf__: Any

class UserListRuleTypeEnum(proto.Message):
    class UserListRuleType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AND_OF_ORS: int
        OR_OF_ANDS: int
