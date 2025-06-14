import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdNetworkTypeEnum(proto.Message):
    class AdNetworkType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH: int
        SEARCH_PARTNERS: int
        CONTENT: int
        MIXED: int
        YOUTUBE: int
        GOOGLE_TV: int
        GOOGLE_OWNED_CHANNELS: int
