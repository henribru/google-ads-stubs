import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ListOperationErrorEnum(proto.Message):
    class ListOperationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUIRED_FIELD_MISSING: int
        DUPLICATE_VALUES: int
