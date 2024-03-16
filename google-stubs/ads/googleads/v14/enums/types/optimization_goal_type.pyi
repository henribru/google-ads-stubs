from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class OptimizationGoalTypeEnum(proto.Message):
    class OptimizationGoalType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CALL_CLICKS = 2
        DRIVING_DIRECTIONS = 3
        APP_PRE_REGISTRATION = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
