from google.ads.googleads.v23.enums.types.goal_config_level import GoalConfigLevelEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionGoalCampaignConfig(proto.Message):
    resource_name: str
    campaign: str
    goal_config_level: GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign: str = ..., goal_config_level: GoalConfigLevelEnum.GoalConfigLevel = ..., custom_conversion_goal: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "goal_config_level", "custom_conversion_goal"]) -> bool: ...
