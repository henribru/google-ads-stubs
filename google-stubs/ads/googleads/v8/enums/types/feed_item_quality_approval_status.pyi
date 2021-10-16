from typing import Any

import proto

__protobuf__: Any

class FeedItemQualityApprovalStatusEnum(proto.Message):
    class FeedItemQualityApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPROVED: int
        DISAPPROVED: int
