import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class MatchingFunctionOperatorEnum(proto.Message):
    class MatchingFunctionOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IN: int
        IDENTITY: int
        EQUALS: int
        AND: int
        CONTAINS_ANY: int
