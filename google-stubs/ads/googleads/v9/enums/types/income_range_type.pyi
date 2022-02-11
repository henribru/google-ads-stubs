from typing import Any

import proto

__protobuf__: Any

class IncomeRangeTypeEnum(proto.Message):
    class IncomeRangeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INCOME_RANGE_0_50: int
        INCOME_RANGE_50_60: int
        INCOME_RANGE_60_70: int
        INCOME_RANGE_70_80: int
        INCOME_RANGE_80_90: int
        INCOME_RANGE_90_UP: int
        INCOME_RANGE_UNDETERMINED: int
