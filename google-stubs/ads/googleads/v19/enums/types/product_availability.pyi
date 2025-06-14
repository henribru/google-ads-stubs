import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductAvailabilityEnum(proto.Message):
    class ProductAvailability(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IN_STOCK: int
        OUT_OF_STOCK: int
        PREORDER: int
