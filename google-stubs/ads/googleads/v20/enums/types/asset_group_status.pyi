import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetGroupStatusEnum(proto.Message):
    class AssetGroupStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
