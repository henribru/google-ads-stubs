import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CollectionSizeErrorEnum(proto.Message):
    class CollectionSizeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_FEW: int
        TOO_MANY: int
