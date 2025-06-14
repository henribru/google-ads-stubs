import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class HotelReconciliationStatusEnum(proto.Message):
    class HotelReconciliationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RESERVATION_ENABLED: int
        RECONCILIATION_NEEDED: int
        RECONCILED: int
        CANCELED: int
