import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BudgetTypeEnum(proto.Message):
    class BudgetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STANDARD: int
        FIXED_CPA: int
        SMART_CAMPAIGN: int
        LOCAL_SERVICES: int
