from typing import Any

import proto

__protobuf__: Any

class PolicyApprovalStatusEnum(proto.Message):
    class PolicyApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISAPPROVED: int
        APPROVED_LIMITED: int
        APPROVED: int
        AREA_OF_INTEREST_ONLY: int
