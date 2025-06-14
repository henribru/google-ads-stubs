import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductIssueSeverityEnum(proto.Message):
    class ProductIssueSeverity(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WARNING: int
        ERROR: int
