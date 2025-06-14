import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PositiveGeoTargetTypeEnum(proto.Message):
    class PositiveGeoTargetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PRESENCE_OR_INTEREST: int
        SEARCH_INTEREST: int
        PRESENCE: int
