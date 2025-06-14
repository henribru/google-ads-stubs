import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BillingSetupStatusEnum(proto.Message):
    class BillingSetupStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED_HELD: int
        APPROVED: int
        CANCELLED: int
