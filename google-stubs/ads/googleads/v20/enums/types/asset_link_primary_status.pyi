import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetLinkPrimaryStatusEnum(proto.Message):
    class AssetLinkPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        PENDING: int
        LIMITED: int
        NOT_ELIGIBLE: int
