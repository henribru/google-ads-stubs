import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SharedSetTypeEnum(proto.Message):
    class SharedSetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEGATIVE_KEYWORDS: int
        NEGATIVE_PLACEMENTS: int
        ACCOUNT_LEVEL_NEGATIVE_KEYWORDS: int
        BRANDS: int
