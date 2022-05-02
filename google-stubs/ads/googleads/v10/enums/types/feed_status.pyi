import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FeedStatusEnum(proto.Message):
    class FeedStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
