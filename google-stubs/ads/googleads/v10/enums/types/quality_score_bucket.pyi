import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class QualityScoreBucketEnum(proto.Message):
    class QualityScoreBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BELOW_AVERAGE: int
        AVERAGE: int
        ABOVE_AVERAGE: int
