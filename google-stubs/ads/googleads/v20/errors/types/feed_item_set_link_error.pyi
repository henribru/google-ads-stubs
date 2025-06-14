import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FeedItemSetLinkErrorEnum(proto.Message):
    class FeedItemSetLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ID_MISMATCH: int
        NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET: int
