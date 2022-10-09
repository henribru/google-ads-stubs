import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class QuotaErrorEnum(proto.Message):
    class QuotaError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RESOURCE_EXHAUSTED: int
        ACCESS_PROHIBITED: int
        RESOURCE_TEMPORARILY_EXHAUSTED: int
