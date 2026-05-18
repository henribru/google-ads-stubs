from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerLifecycleGoalErrorEnum(proto.Message):
    class CustomerLifecycleGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_ACQUISITION_VALUE_MISSING = 2
        CUSTOMER_ACQUISITION_INVALID_VALUE = 3
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE = 4
        CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED = 5
        CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED = 6
        INVALID_EXISTING_USER_LIST = 7
        INVALID_HIGH_LIFETIME_VALUE_USER_LIST = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
