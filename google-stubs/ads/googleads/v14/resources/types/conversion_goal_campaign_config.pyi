from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.goal_config_level import GoalConfigLevelEnum

_M = TypeVar("_M")

class ConversionGoalCampaignConfig(proto.Message):
    resource_name: str
    campaign: str
    goal_config_level: GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        goal_config_level: GoalConfigLevelEnum.GoalConfigLevel = ...,
        custom_conversion_goal: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "campaign", "goal_config_level", "custom_conversion_goal"
        ],
    ) -> bool: ...
