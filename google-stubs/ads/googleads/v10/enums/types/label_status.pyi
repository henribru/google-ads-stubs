import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LabelStatusEnum(proto.Message):
    class LabelStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
