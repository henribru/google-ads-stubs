import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionGoalCampaignConfigErrorEnum(proto.Message):
    class ConversionGoalCampaignConfigError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: int
        CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER: int
        CAMPAIGN_CANNOT_USE_UNIFIED_GOALS: int
