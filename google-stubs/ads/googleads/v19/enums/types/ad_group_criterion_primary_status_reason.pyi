import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupCriterionPrimaryStatusReasonEnum(proto.Message):
    class AdGroupCriterionPrimaryStatusReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_PENDING: int
        CAMPAIGN_CRITERION_NEGATIVE: int
        CAMPAIGN_PAUSED: int
        CAMPAIGN_REMOVED: int
        CAMPAIGN_ENDED: int
        AD_GROUP_PAUSED: int
        AD_GROUP_REMOVED: int
        AD_GROUP_CRITERION_DISAPPROVED: int
        AD_GROUP_CRITERION_RARELY_SERVED: int
        AD_GROUP_CRITERION_LOW_QUALITY: int
        AD_GROUP_CRITERION_UNDER_REVIEW: int
        AD_GROUP_CRITERION_PENDING_REVIEW: int
        AD_GROUP_CRITERION_BELOW_FIRST_PAGE_BID: int
        AD_GROUP_CRITERION_NEGATIVE: int
        AD_GROUP_CRITERION_RESTRICTED: int
        AD_GROUP_CRITERION_PAUSED: int
        AD_GROUP_CRITERION_PAUSED_DUE_TO_LOW_ACTIVITY: int
        AD_GROUP_CRITERION_REMOVED: int
