import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DataDrivenModelStatusEnum(proto.Message):
    class DataDrivenModelStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AVAILABLE: int
        STALE: int
        EXPIRED: int
        NEVER_GENERATED: int
