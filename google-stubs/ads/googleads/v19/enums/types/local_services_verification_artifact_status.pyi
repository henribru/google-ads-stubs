import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesVerificationArtifactStatusEnum(proto.Message):
    class LocalServicesVerificationArtifactStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PASSED: int
        FAILED: int
        PENDING: int
        NO_SUBMISSION: int
        CANCELLED: int
