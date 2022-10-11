import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AudienceStatusEnum(proto.Message):
    class AudienceStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
