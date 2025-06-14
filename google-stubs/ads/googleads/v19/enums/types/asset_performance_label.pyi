import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetPerformanceLabelEnum(proto.Message):
    class AssetPerformanceLabel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        LEARNING: int
        LOW: int
        GOOD: int
        BEST: int
