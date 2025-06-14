import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FeedAttributeReferenceErrorEnum(proto.Message):
    class FeedAttributeReferenceError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_REFERENCE_REMOVED_FEED: int
        INVALID_FEED_NAME: int
        INVALID_FEED_ATTRIBUTE_NAME: int
