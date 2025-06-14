import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ResourceChangeOperationEnum(proto.Message):
    class ResourceChangeOperation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREATE: int
        UPDATE: int
        REMOVE: int
