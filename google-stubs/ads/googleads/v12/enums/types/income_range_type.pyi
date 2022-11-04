from typing import Any

import proto

class IncomeRangeTypeEnum(proto.Message):
    class IncomeRangeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INCOME_RANGE_0_50 = 510001
        INCOME_RANGE_50_60 = 510002
        INCOME_RANGE_60_70 = 510003
        INCOME_RANGE_70_80 = 510004
        INCOME_RANGE_80_90 = 510005
        INCOME_RANGE_90_UP = 510006
        INCOME_RANGE_UNDETERMINED = 510000
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
