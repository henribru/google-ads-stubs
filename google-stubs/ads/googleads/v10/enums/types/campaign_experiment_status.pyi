import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignExperimentStatusEnum(proto.Message):
    class CampaignExperimentStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INITIALIZING: int
        INITIALIZATION_FAILED: int
        ENABLED: int
        GRADUATED: int
        REMOVED: int
        PROMOTING: int
        PROMOTION_FAILED: int
        PROMOTED: int
        ENDED_MANUALLY: int
