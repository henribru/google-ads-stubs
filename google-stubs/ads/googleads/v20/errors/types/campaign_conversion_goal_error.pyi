import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CampaignConversionGoalErrorEnum(proto.Message):
    class CampaignConversionGoalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: int
        CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN: int
