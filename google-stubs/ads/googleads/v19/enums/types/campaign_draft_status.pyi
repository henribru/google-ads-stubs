import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignDraftStatusEnum(proto.Message):
    class CampaignDraftStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROPOSED: int
        REMOVED: int
        PROMOTING: int
        PROMOTED: int
        PROMOTE_FAILED: int
