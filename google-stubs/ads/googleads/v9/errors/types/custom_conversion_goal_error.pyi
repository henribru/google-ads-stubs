from typing import Any

import proto

__protobuf__: Any

class CustomConversionGoalErrorEnum(proto.Message):
    class CustomConversionGoalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_CONVERSION_ACTION: int
        CONVERSION_ACTION_NOT_ENABLED: int
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL: int
