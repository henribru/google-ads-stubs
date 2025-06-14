import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BatchJobStatusEnum(proto.Message):
    class BatchJobStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        RUNNING: int
        DONE: int
