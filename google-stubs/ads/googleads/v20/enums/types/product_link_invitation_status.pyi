import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductLinkInvitationStatusEnum(proto.Message):
    class ProductLinkInvitationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCEPTED: int
        REQUESTED: int
        PENDING_APPROVAL: int
        REVOKED: int
        REJECTED: int
        EXPIRED: int
