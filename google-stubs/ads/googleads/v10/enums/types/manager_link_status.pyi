import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ManagerLinkStatusEnum(proto.Message):
    class ManagerLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTIVE: int
        INACTIVE: int
        PENDING: int
        REFUSED: int
        CANCELED: int
