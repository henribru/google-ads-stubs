import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ChangeStatusOperationEnum(proto.Message):
    class ChangeStatusOperation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADDED: int
        CHANGED: int
        REMOVED: int
