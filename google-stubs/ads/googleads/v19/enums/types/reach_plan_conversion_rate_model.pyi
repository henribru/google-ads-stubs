import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ReachPlanConversionRateModelEnum(proto.Message):
    class ReachPlanConversionRateModel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_HISTORY: int
        INVENTORY_AGGRESSIVE: int
        INVENTORY_CONSERVATIVE: int
        INVENTORY_MEDIAN: int
