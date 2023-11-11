from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ExperimentMetricDirectionEnum(proto.Message):
    class ExperimentMetricDirection(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_CHANGE = 2
        INCREASE = 3
        DECREASE = 4
        NO_CHANGE_OR_INCREASE = 5
        NO_CHANGE_OR_DECREASE = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
