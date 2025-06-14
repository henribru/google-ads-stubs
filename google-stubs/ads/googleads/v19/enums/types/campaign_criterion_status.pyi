import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignCriterionStatusEnum(proto.Message):
    class CampaignCriterionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
