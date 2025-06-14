import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BrandStateEnum(proto.Message):
    class BrandState(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        DEPRECATED: int
        UNVERIFIED: int
        APPROVED: int
        CANCELLED: int
        REJECTED: int
