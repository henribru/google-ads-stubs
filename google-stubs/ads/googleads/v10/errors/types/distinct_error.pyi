import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DistinctErrorEnum(proto.Message):
    class DistinctError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_ELEMENT: int
        DUPLICATE_TYPE: int
