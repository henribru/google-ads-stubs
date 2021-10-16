from typing import Any

import proto

__protobuf__: Any

class AccountBudgetProposalStatusEnum(proto.Message):
    class AccountBudgetProposalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED_HELD: int
        APPROVED: int
        CANCELLED: int
        REJECTED: int
