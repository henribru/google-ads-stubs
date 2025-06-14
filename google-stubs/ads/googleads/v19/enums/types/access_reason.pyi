import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccessReasonEnum(proto.Message):
    class AccessReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OWNED: int
        SHARED: int
        LICENSED: int
        SUBSCRIBED: int
        AFFILIATED: int
