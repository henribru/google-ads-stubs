import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetGroupSignalApprovalStatusEnum(proto.Message):
    class AssetGroupSignalApprovalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPROVED: int
        LIMITED: int
        DISAPPROVED: int
        UNDER_REVIEW: int
