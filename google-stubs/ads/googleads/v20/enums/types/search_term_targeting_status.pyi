import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SearchTermTargetingStatusEnum(proto.Message):
    class SearchTermTargetingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADDED: int
        EXCLUDED: int
        ADDED_EXCLUDED: int
        NONE: int
