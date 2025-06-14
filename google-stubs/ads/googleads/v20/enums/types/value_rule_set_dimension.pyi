import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ValueRuleSetDimensionEnum(proto.Message):
    class ValueRuleSetDimension(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GEO_LOCATION: int
        DEVICE: int
        AUDIENCE: int
        NO_CONDITION: int
        ITINERARY: int
