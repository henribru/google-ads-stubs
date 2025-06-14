import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetLinkPrimaryStatusReasonEnum(proto.Message):
    class AssetLinkPrimaryStatusReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ASSET_LINK_PAUSED: int
        ASSET_LINK_REMOVED: int
        ASSET_DISAPPROVED: int
        ASSET_UNDER_REVIEW: int
        ASSET_APPROVED_LABELED: int
