from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomConversionGoalErrorEnum(proto.Message):
    class CustomConversionGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_CONVERSION_ACTION = 2
        CONVERSION_ACTION_NOT_ENABLED = 3
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL = 4
        CUSTOM_GOAL_DUPLICATE_NAME = 5
        DUPLICATE_CONVERSION_ACTION_LIST = 6
        NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
