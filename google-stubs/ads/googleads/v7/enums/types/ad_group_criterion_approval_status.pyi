from typing import Any

import proto

__protobuf__: Any

class AdGroupCriterionApprovalStatusEnum(proto.Message):
    class AdGroupCriterionApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPROVED: int
        DISAPPROVED: int
        PENDING_REVIEW: int
        UNDER_REVIEW: int
