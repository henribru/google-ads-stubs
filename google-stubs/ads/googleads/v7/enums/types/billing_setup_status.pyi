from typing import Any

import proto

__protobuf__: Any

class BillingSetupStatusEnum(proto.Message):
    class BillingSetupStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        APPROVED_HELD: int
        APPROVED: int
        CANCELLED: int
