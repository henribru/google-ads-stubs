from typing import Any

import proto

class CustomAudienceErrorEnum(proto.Message):
    class CustomAudienceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NAME_ALREADY_USED = 2
        CANNOT_REMOVE_WHILE_IN_USE = 3
        RESOURCE_ALREADY_REMOVED = 4
        MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED = 5
        INVALID_MEMBER_TYPE = 6
        MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH = 7
        POLICY_VIOLATION = 8
        INVALID_TYPE_CHANGE = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
