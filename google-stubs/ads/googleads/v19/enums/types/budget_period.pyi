import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BudgetPeriodEnum(proto.Message):
    class BudgetPeriod(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DAILY: int
        CUSTOM_PERIOD: int
