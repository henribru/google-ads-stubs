import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerFeedErrorEnum(proto.Message):
    class CustomerFeedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: int
        CANNOT_CREATE_FOR_REMOVED_FEED: int
        CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED: int
        CANNOT_MODIFY_REMOVED_CUSTOMER_FEED: int
        INVALID_PLACEHOLDER_TYPE: int
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: int
        PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED: int
