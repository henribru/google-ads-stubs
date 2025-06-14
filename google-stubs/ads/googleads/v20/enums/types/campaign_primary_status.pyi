import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignPrimaryStatusEnum(proto.Message):
    class CampaignPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        ENDED: int
        PENDING: int
        MISCONFIGURED: int
        LIMITED: int
        LEARNING: int
        NOT_ELIGIBLE: int
