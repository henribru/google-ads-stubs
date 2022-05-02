import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignServingStatusEnum(proto.Message):
    class CampaignServingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SERVING: int
        NONE: int
        ENDED: int
        PENDING: int
        SUSPENDED: int
