from typing import Any

import proto

__protobuf__: Any

class BudgetDeliveryMethodEnum(proto.Message):
    class BudgetDeliveryMethod(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STANDARD: int
        ACCELERATED: int
