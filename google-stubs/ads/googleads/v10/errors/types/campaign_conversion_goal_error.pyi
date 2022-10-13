from typing import Any

import proto

class CampaignConversionGoalErrorEnum(proto.Message):
    class CampaignConversionGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
