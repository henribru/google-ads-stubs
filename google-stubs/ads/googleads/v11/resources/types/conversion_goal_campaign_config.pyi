from typing import Any

import proto

from google.ads.googleads.v11.enums.types.goal_config_level import GoalConfigLevelEnum

class ConversionGoalCampaignConfig(proto.Message):
    resource_name: str
    campaign: str
    goal_config_level: GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        goal_config_level: GoalConfigLevelEnum.GoalConfigLevel = ...,
        custom_conversion_goal: str = ...
    ) -> None: ...
