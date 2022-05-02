import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class InternalErrorEnum(proto.Message):
    class InternalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INTERNAL_ERROR: int
        ERROR_CODE_NOT_PUBLISHED: int
        TRANSIENT_ERROR: int
        DEADLINE_EXCEEDED: int
