import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccountLinkStatusEnum(proto.Message):
    class AccountLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        REQUESTED: int
        PENDING_APPROVAL: int
        REJECTED: int
        REVOKED: int
