import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionActionStatusEnum(proto.Message):
    class ConversionActionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        HIDDEN: int
