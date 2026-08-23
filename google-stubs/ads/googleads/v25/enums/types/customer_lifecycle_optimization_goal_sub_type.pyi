from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerLifecycleOptimizationGoalSubTypeEnum(proto.Message):
    class CustomerLifecycleOptimizationGoalSubType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW_CUSTOMER_ACQUISITION_VALUE = 2
        NEW_CUSTOMER_ACQUISITION_ONLY = 3
        CUSTOMER_RETENTION_VALUE = 4
        CUSTOMER_RETENTION_ONLY = 5
        LOYALTY_RETENTION_VALUE = 7
        LOYALTY_RETENTION_BENEFITS = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
