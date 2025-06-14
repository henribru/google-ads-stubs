import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupPrimaryStatusEnum(proto.Message):
    class AdGroupPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        PENDING: int
        NOT_ELIGIBLE: int
        LIMITED: int
