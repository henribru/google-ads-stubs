import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdSharingErrorEnum(proto.Message):
    class AdSharingError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_ALREADY_CONTAINS_AD: int
        INCOMPATIBLE_AD_UNDER_AD_GROUP: int
        CANNOT_SHARE_INACTIVE_AD: int
