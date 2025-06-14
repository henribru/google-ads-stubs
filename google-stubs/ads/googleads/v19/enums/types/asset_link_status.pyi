import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetLinkStatusEnum(proto.Message):
    class AssetLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        PAUSED: int
