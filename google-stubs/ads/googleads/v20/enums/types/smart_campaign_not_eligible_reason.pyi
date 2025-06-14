import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SmartCampaignNotEligibleReasonEnum(proto.Message):
    class SmartCampaignNotEligibleReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCOUNT_ISSUE: int
        BILLING_ISSUE: int
        BUSINESS_PROFILE_LOCATION_REMOVED: int
        ALL_ADS_DISAPPROVED: int
