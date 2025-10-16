from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordPlanErrorEnum(proto.Message):
    class KeywordPlanError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BID_MULTIPLIER_OUT_OF_RANGE = 2
        BID_TOO_HIGH = 3
        BID_TOO_LOW = 4
        BID_TOO_MANY_FRACTIONAL_DIGITS = 5
        DAILY_BUDGET_TOO_LOW = 6
        DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS = 7
        INVALID_VALUE = 8
        KEYWORD_PLAN_HAS_NO_KEYWORDS = 9
        KEYWORD_PLAN_NOT_ENABLED = 10
        KEYWORD_PLAN_NOT_FOUND = 11
        MISSING_BID = 13
        MISSING_FORECAST_PERIOD = 14
        INVALID_FORECAST_DATE_RANGE = 15
        INVALID_NAME = 16

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
