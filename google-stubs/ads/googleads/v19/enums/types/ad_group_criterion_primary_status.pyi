import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupCriterionPrimaryStatusEnum(proto.Message):
    class AdGroupCriterionPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        PENDING: int
        NOT_ELIGIBLE: int
