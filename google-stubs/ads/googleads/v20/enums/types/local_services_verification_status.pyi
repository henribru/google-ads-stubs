import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesVerificationStatusEnum(proto.Message):
    class LocalServicesVerificationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEEDS_REVIEW: int
        FAILED: int
        PASSED: int
        NOT_APPLICABLE: int
        NO_SUBMISSION: int
        PARTIAL_SUBMISSION: int
        PENDING_ESCALATION: int
