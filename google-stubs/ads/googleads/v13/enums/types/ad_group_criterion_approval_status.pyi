from typing import Any

import proto

class AdGroupCriterionApprovalStatusEnum(proto.Message):
    class AdGroupCriterionApprovalStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPROVED = 2
        DISAPPROVED = 3
        PENDING_REVIEW = 4
        UNDER_REVIEW = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
