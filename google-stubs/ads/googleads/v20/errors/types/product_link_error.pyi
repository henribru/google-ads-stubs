import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductLinkErrorEnum(proto.Message):
    class ProductLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_OPERATION: int
        CREATION_NOT_PERMITTED: int
        INVITATION_EXISTS: int
        LINK_EXISTS: int
