import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class IdentityVerificationProgramStatusEnum(proto.Message):
    class IdentityVerificationProgramStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING_USER_ACTION: int
        PENDING_REVIEW: int
        SUCCESS: int
        FAILURE: int
