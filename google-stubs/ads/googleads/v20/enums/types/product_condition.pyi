import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductConditionEnum(proto.Message):
    class ProductCondition(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEW: int
        REFURBISHED: int
        USED: int
