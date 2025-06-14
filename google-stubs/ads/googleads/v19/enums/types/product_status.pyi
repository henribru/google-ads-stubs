import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductStatusEnum(proto.Message):
    class ProductStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_ELIGIBLE: int
        ELIGIBLE_LIMITED: int
        ELIGIBLE: int
