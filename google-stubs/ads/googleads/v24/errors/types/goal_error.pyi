from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class GoalErrorEnum(proto.Message):
    class GoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RETENTION_GOAL_ALREADY_EXISTS = 4
        HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT = 5
        HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE = 6
        CUSTOMER_LIFECYCLE_OPTIMIZATION_ACCOUNT_TYPE_NOT_ALLOWED = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
