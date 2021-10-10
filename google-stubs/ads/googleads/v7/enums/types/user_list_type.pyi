from typing import Any

import proto

__protobuf__: Any

class UserListTypeEnum(proto.Message):
    class UserListType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REMARKETING: int
        LOGICAL: int
        EXTERNAL_REMARKETING: int
        RULE_BASED: int
        SIMILAR: int
        CRM_BASED: int
