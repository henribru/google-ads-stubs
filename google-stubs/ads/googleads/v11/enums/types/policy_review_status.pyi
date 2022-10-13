from typing import Any

import proto

class PolicyReviewStatusEnum(proto.Message):
    class PolicyReviewStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REVIEW_IN_PROGRESS = 2
        REVIEWED = 3
        UNDER_APPEAL = 4
        ELIGIBLE_MAY_SERVE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
