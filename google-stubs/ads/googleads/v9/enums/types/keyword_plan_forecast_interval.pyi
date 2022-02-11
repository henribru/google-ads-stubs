from typing import Any

import proto

__protobuf__: Any

class KeywordPlanForecastIntervalEnum(proto.Message):
    class KeywordPlanForecastInterval(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEXT_WEEK: int
        NEXT_MONTH: int
        NEXT_QUARTER: int
