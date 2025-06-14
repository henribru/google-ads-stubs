import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupAdPrimaryStatusReasonEnum(proto.Message):
    class AdGroupAdPrimaryStatusReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_REMOVED: int
        CAMPAIGN_PAUSED: int
        CAMPAIGN_PENDING: int
        CAMPAIGN_ENDED: int
        AD_GROUP_PAUSED: int
        AD_GROUP_REMOVED: int
        AD_GROUP_AD_PAUSED: int
        AD_GROUP_AD_REMOVED: int
        AD_GROUP_AD_DISAPPROVED: int
        AD_GROUP_AD_UNDER_REVIEW: int
        AD_GROUP_AD_POOR_QUALITY: int
        AD_GROUP_AD_NO_ADS: int
        AD_GROUP_AD_APPROVED_LABELED: int
        AD_GROUP_AD_AREA_OF_INTEREST_ONLY: int
        AD_GROUP_AD_UNDER_APPEAL: int
