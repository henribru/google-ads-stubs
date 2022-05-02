import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdServingOptimizationStatusEnum(proto.Message):
    class AdServingOptimizationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPTIMIZE: int
        CONVERSION_OPTIMIZE: int
        ROTATE: int
        ROTATE_INDEFINITELY: int
        UNAVAILABLE: int
