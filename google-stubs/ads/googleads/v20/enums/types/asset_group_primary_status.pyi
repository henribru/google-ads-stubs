import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetGroupPrimaryStatusEnum(proto.Message):
    class AssetGroupPrimaryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        PAUSED: int
        REMOVED: int
        NOT_ELIGIBLE: int
        LIMITED: int
        PENDING: int
