from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class KeywordPlanForecastIntervalEnum(proto.Message):
    class KeywordPlanForecastInterval(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEXT_WEEK = 3
        NEXT_MONTH = 4
        NEXT_QUARTER = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
