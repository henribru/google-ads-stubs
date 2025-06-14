import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupPrimaryStatusReasonEnum(proto.Message):
    class AdGroupPrimaryStatusReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_REMOVED: int
        CAMPAIGN_PAUSED: int
        CAMPAIGN_PENDING: int
        CAMPAIGN_ENDED: int
        AD_GROUP_PAUSED: int
        AD_GROUP_REMOVED: int
        AD_GROUP_INCOMPLETE: int
        KEYWORDS_PAUSED: int
        NO_KEYWORDS: int
        AD_GROUP_ADS_PAUSED: int
        NO_AD_GROUP_ADS: int
        HAS_ADS_DISAPPROVED: int
        HAS_ADS_LIMITED_BY_POLICY: int
        MOST_ADS_UNDER_REVIEW: int
        CAMPAIGN_DRAFT: int
        AD_GROUP_PAUSED_DUE_TO_LOW_ACTIVITY: int
