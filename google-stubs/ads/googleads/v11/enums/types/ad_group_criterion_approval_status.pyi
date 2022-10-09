import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupCriterionApprovalStatusEnum(proto.Message):
    class AdGroupCriterionApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPROVED: int
        DISAPPROVED: int
        PENDING_REVIEW: int
        UNDER_REVIEW: int
