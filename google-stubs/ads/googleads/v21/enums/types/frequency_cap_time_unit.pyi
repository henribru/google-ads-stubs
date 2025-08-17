from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FrequencyCapTimeUnitEnum(proto.Message):
    class FrequencyCapTimeUnit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DAY = 2
        WEEK = 3
        MONTH = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
