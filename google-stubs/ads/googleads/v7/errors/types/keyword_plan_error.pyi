from typing import Any

import proto

__protobuf__: Any

class KeywordPlanErrorEnum(proto.Message):
    class KeywordPlanError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BID_MULTIPLIER_OUT_OF_RANGE: int
        BID_TOO_HIGH: int
        BID_TOO_LOW: int
        BID_TOO_MANY_FRACTIONAL_DIGITS: int
        DAILY_BUDGET_TOO_LOW: int
        DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS: int
        INVALID_VALUE: int
        KEYWORD_PLAN_HAS_NO_KEYWORDS: int
        KEYWORD_PLAN_NOT_ENABLED: int
        KEYWORD_PLAN_NOT_FOUND: int
        MISSING_BID: int
        MISSING_FORECAST_PERIOD: int
        INVALID_FORECAST_DATE_RANGE: int
        INVALID_NAME: int
