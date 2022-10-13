from typing import Any

import proto

class PolicyApprovalStatusEnum(proto.Message):
    class PolicyApprovalStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DISAPPROVED = 2
        APPROVED_LIMITED = 3
        APPROVED = 4
        AREA_OF_INTEREST_ONLY = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
