from typing import Any

import proto

__protobuf__: Any

class HotelReconciliationStatusEnum(proto.Message):
    class HotelReconciliationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RESERVATION_ENABLED: int
        RECONCILIATION_NEEDED: int
        RECONCILED: int
        CANCELED: int
