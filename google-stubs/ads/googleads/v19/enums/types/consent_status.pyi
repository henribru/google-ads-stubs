import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConsentStatusEnum(proto.Message):
    class ConsentStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GRANTED: int
        DENIED: int
