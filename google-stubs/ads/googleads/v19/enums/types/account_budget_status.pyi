import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccountBudgetStatusEnum(proto.Message):
    class AccountBudgetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED: int
        CANCELLED: int
