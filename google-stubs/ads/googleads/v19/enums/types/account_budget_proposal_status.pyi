import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccountBudgetProposalStatusEnum(proto.Message):
    class AccountBudgetProposalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED_HELD: int
        APPROVED: int
        CANCELLED: int
        REJECTED: int
