from typing import Any

import proto

__protobuf__: Any

class CustomAudienceErrorEnum(proto.Message):
    class CustomAudienceError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NAME_ALREADY_USED: int
        CANNOT_REMOVE_WHILE_IN_USE: int
        RESOURCE_ALREADY_REMOVED: int
        MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED: int
        INVALID_MEMBER_TYPE: int
        MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH: int
        POLICY_VIOLATION: int
        INVALID_TYPE_CHANGE: int
