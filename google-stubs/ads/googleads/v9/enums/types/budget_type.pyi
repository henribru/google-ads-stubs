from typing import Any

import proto

__protobuf__: Any

class BudgetTypeEnum(proto.Message):
    class BudgetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STANDARD: int
        FIXED_CPA: int
        SMART_CAMPAIGN: int
