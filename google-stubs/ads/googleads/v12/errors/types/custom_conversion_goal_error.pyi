from typing import Any

import proto

class CustomConversionGoalErrorEnum(proto.Message):
    class CustomConversionGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_CONVERSION_ACTION = 2
        CONVERSION_ACTION_NOT_ENABLED = 3
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL = 4
        CUSTOM_GOAL_DUPLICATE_NAME = 5
        DUPLICATE_CONVERSION_ACTION_LIST = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
