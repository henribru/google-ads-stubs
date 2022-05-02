import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AsyncActionStatusEnum(proto.Message):
    class AsyncActionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_STARTED: int
        IN_PROGRESS: int
        COMPLETED: int
        FAILED: int
        COMPLETED_WITH_WARNING: int
