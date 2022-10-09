import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ContextErrorEnum(proto.Message):
    class ContextError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPERATION_NOT_PERMITTED_FOR_CONTEXT: int
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: int
