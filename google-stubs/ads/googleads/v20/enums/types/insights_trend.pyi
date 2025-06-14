import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class InsightsTrendEnum(proto.Message):
    class InsightsTrend(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EMERGING: int
        RISING: int
        SUSTAINED: int
        DECLINING: int
