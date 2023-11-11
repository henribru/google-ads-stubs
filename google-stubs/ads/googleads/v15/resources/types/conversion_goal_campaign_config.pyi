from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.goal_config_level import GoalConfigLevelEnum

_M = TypeVar("_M")

class ConversionGoalCampaignConfig(proto.Message):
    resource_name: str
    campaign: str
    goal_config_level: GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        goal_config_level: GoalConfigLevelEnum.GoalConfigLevel = ...,
        custom_conversion_goal: str = ...
    ) -> None: ...
