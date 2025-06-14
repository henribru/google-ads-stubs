import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccountLinkErrorEnum(proto.Message):
    class AccountLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_STATUS: int
        PERMISSION_DENIED: int
