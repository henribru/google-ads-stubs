import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class TimeTypeEnum(proto.Message):
    class TimeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOW: int
        FOREVER: int
