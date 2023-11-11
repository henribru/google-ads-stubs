from typing import Any

import proto

class ConversionGoalCampaignConfigErrorEnum(proto.Message):
    class ConversionGoalCampaignConfigError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN = 2
        CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER = 3
        CAMPAIGN_CANNOT_USE_UNIFIED_GOALS = 4
        EMPTY_CONVERSION_GOALS = 5
        STORE_SALE_STORE_VISIT_CANNOT_BE_BOTH_INCLUDED = 6
        PERFORMANCE_MAX_CAMPAIGN_CANNOT_USE_CUSTOM_GOAL_WITH_STORE_SALES = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
