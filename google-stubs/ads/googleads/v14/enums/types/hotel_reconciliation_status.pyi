from typing import Any

import proto

class HotelReconciliationStatusEnum(proto.Message):
    class HotelReconciliationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESERVATION_ENABLED = 2
        RECONCILIATION_NEEDED = 3
        RECONCILED = 4
        CANCELED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
