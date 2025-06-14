import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SmartCampaignStatusEnum(proto.Message):
    class SmartCampaignStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PAUSED: int
        NOT_ELIGIBLE: int
        PENDING: int
        ELIGIBLE: int
        REMOVED: int
        ENDED: int
