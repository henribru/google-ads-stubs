import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class TargetingDimensionEnum(proto.Message):
    class TargetingDimension(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        KEYWORD: int
        AUDIENCE: int
        TOPIC: int
        GENDER: int
        AGE_RANGE: int
        PLACEMENT: int
        PARENTAL_STATUS: int
        INCOME_RANGE: int
