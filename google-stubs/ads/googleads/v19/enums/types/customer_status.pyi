import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerStatusEnum(proto.Message):
    class CustomerStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        CANCELED: int
        SUSPENDED: int
        CLOSED: int
