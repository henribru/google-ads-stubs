from google.ads.googleads.v22.common.types.goal_setting import GoalSetting
from google.ads.googleads.v22.enums.types.goal_optimization_eligibility import GoalOptimizationEligibilityEnum
from google.ads.googleads.v22.enums.types.goal_type import GoalTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class Goal(proto.Message):
    resource_name: str
    goal_id: int
    goal_type: GoalTypeEnum.GoalType
    owner_customer: str
    optimization_eligibility: GoalOptimizationEligibilityEnum.GoalOptimizationEligibility
    retention_goal_settings: GoalSetting.RetentionGoal
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., goal_id: int = ..., goal_type: GoalTypeEnum.GoalType = ..., owner_customer: str = ..., optimization_eligibility: GoalOptimizationEligibilityEnum.GoalOptimizationEligibility = ..., retention_goal_settings: GoalSetting.RetentionGoal = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "goal_id", "goal_type", "owner_customer", "optimization_eligibility", "retention_goal_settings"]) -> bool: ...
