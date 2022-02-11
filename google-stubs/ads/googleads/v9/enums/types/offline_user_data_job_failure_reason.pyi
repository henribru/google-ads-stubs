from typing import Any

import proto

__protobuf__: Any

class OfflineUserDataJobFailureReasonEnum(proto.Message):
    class OfflineUserDataJobFailureReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INSUFFICIENT_MATCHED_TRANSACTIONS: int
        INSUFFICIENT_TRANSACTIONS: int
