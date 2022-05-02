import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class OfflineUserDataJobStatusEnum(proto.Message):
    class OfflineUserDataJobStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        RUNNING: int
        SUCCESS: int
        FAILED: int
