import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccessInvitationStatusEnum(proto.Message):
    class AccessInvitationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        DECLINED: int
        EXPIRED: int
