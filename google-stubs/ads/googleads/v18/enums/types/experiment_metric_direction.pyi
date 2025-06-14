import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
