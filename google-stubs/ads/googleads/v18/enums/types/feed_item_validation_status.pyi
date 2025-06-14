import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FeedItemValidationStatusEnum(proto.Message):
    class FeedItemValidationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        INVALID: int
        VALID: int
