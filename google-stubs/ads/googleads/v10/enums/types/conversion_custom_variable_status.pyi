import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionCustomVariableStatusEnum(proto.Message):
    class ConversionCustomVariableStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTIVATION_NEEDED: int
        ENABLED: int
        PAUSED: int
