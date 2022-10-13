from typing import Any

import proto

class OfflineUserDataJobFailureReasonEnum(proto.Message):
    class OfflineUserDataJobFailureReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INSUFFICIENT_MATCHED_TRANSACTIONS = 2
        INSUFFICIENT_TRANSACTIONS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
