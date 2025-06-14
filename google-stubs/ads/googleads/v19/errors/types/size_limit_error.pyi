import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SizeLimitErrorEnum(proto.Message):
    class SizeLimitError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUEST_SIZE_LIMIT_EXCEEDED: int
        RESPONSE_SIZE_LIMIT_EXCEEDED: int
