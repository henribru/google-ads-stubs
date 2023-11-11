from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ReachPlanErrorEnum(proto.Message):
    class ReachPlanError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_FORECASTABLE_MISSING_RATE = 2
        NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY = 3
        NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
