import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class KeywordMatchTypeEnum(proto.Message):
    class KeywordMatchType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXACT: int
        PHRASE: int
        BROAD: int
