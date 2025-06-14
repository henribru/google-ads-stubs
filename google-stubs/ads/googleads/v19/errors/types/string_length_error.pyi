import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class StringLengthErrorEnum(proto.Message):
    class StringLengthError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EMPTY: int
        TOO_SHORT: int
        TOO_LONG: int
