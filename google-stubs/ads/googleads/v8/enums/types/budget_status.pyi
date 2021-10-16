from typing import Any

import proto

__protobuf__: Any

class BudgetStatusEnum(proto.Message):
    class BudgetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
