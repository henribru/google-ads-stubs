import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DataLinkStatusEnum(proto.Message):
    class DataLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUESTED: int
        PENDING_APPROVAL: int
        ENABLED: int
        DISABLED: int
        REVOKED: int
        REJECTED: int
