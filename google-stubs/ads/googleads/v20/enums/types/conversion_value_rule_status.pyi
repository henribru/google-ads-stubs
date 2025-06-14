import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionValueRuleStatusEnum(proto.Message):
    class ConversionValueRuleStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        PAUSED: int
