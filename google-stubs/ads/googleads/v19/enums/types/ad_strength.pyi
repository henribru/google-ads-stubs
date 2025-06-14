import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdStrengthEnum(proto.Message):
    class AdStrength(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        NO_ADS: int
        POOR: int
        AVERAGE: int
        GOOD: int
        EXCELLENT: int
