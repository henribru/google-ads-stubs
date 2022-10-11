import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class StringFormatErrorEnum(proto.Message):
    class StringFormatError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ILLEGAL_CHARS: int
        INVALID_FORMAT: int
