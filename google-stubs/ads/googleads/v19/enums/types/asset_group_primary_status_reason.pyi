import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetGroupPrimaryStatusReasonEnum(proto.Message):
    class AssetGroupPrimaryStatusReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ASSET_GROUP_PAUSED: int
        ASSET_GROUP_REMOVED: int
        CAMPAIGN_REMOVED: int
        CAMPAIGN_PAUSED: int
        CAMPAIGN_PENDING: int
        CAMPAIGN_ENDED: int
        ASSET_GROUP_LIMITED: int
        ASSET_GROUP_DISAPPROVED: int
        ASSET_GROUP_UNDER_REVIEW: int
