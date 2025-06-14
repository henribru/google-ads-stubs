import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdServingOptimizationStatusEnum(proto.Message):
    class AdServingOptimizationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTIMIZE = 2
        CONVERSION_OPTIMIZE = 3
        ROTATE = 4
        ROTATE_INDEFINITELY = 5
        UNAVAILABLE = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
