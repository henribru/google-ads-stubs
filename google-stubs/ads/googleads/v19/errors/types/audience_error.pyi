import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AudienceErrorEnum(proto.Message):
    class AudienceError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NAME_ALREADY_IN_USE: int
        DIMENSION_INVALID: int
        AUDIENCE_SEGMENT_NOT_FOUND: int
        AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED: int
        DUPLICATE_AUDIENCE_SEGMENT: int
        TOO_MANY_SEGMENTS: int
        TOO_MANY_DIMENSIONS_OF_SAME_TYPE: int
        IN_USE: int
        MISSING_ASSET_GROUP_ID: int
        CANNOT_CHANGE_FROM_CUSTOMER_TO_ASSET_GROUP_SCOPE: int
