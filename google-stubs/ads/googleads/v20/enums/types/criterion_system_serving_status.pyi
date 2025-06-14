import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CriterionSystemServingStatusEnum(proto.Message):
    class CriterionSystemServingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        RARELY_SERVED: int
