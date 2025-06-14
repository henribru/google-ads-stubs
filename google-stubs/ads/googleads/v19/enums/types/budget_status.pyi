import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BudgetStatusEnum(proto.Message):
    class BudgetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
