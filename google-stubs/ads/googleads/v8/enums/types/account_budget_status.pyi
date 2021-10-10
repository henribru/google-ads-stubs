from typing import Any

import proto

__protobuf__: Any

class AccountBudgetStatusEnum(proto.Message):
    class AccountBudgetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED: int
        CANCELLED: int
