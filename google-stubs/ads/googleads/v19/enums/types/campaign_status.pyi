import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignStatusEnum(proto.Message):
    class CampaignStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
