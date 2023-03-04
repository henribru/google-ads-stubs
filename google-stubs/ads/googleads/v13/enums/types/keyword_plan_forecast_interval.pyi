from typing import Any

import proto

class KeywordPlanForecastIntervalEnum(proto.Message):
    class KeywordPlanForecastInterval(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEXT_WEEK = 3
        NEXT_MONTH = 4
        NEXT_QUARTER = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
