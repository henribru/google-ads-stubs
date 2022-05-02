import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class OfflineUserDataJobFailureReasonEnum(proto.Message):
    class OfflineUserDataJobFailureReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INSUFFICIENT_MATCHED_TRANSACTIONS: int
        INSUFFICIENT_TRANSACTIONS: int
