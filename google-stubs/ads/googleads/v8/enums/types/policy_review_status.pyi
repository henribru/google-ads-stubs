from typing import Any

import proto

__protobuf__: Any

class PolicyReviewStatusEnum(proto.Message):
    class PolicyReviewStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REVIEW_IN_PROGRESS: int
        REVIEWED: int
        UNDER_APPEAL: int
        ELIGIBLE_MAY_SERVE: int
