import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DatabaseErrorEnum(proto.Message):
    class DatabaseError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONCURRENT_MODIFICATION: int
        DATA_CONSTRAINT_VIOLATION: int
        REQUEST_TOO_LARGE: int
