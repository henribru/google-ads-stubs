from typing import Any

import proto

__protobuf__: Any

class CustomInterestErrorEnum(proto.Message):
    class CustomInterestError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NAME_ALREADY_USED: int
        CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE: int
        TYPE_AND_PARAMETER_NOT_FOUND: int
        TYPE_AND_PARAMETER_ALREADY_EXISTED: int
        INVALID_CUSTOM_INTEREST_MEMBER_TYPE: int
        CANNOT_REMOVE_WHILE_IN_USE: int
        CANNOT_CHANGE_TYPE: int
