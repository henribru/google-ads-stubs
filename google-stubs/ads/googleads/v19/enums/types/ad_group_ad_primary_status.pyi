import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupAdPrimaryStatusEnum(proto.Message):
    class AdGroupAdPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        PENDING: int
        LIMITED: int
        NOT_ELIGIBLE: int
