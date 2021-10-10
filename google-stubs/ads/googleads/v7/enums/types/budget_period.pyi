from typing import Any

import proto

__protobuf__: Any

class BudgetPeriodEnum(proto.Message):
    class BudgetPeriod(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DAILY: int
        CUSTOM_PERIOD: int
