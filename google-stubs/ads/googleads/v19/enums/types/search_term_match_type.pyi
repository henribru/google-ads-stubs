import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SearchTermMatchTypeEnum(proto.Message):
    class SearchTermMatchType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BROAD: int
        EXACT: int
        PHRASE: int
        NEAR_EXACT: int
        NEAR_PHRASE: int
