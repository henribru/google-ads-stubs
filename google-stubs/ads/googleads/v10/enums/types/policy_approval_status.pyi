import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PolicyApprovalStatusEnum(proto.Message):
    class PolicyApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISAPPROVED: int
        APPROVED_LIMITED: int
        APPROVED: int
        AREA_OF_INTEREST_ONLY: int
