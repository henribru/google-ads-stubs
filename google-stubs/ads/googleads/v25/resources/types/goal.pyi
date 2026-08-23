from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.common.types.goal_setting import GoalSetting
from google.ads.googleads.v25.enums.types.goal_optimization_eligibility import (
    GoalOptimizationEligibilityEnum,
)
from google.ads.googleads.v25.enums.types.goal_type import GoalTypeEnum

_M = TypeVar("_M")

class Goal(proto.Message):
    resource_name: str
    goal_id: int
    goal_type: GoalTypeEnum.GoalType
    owner_customer: str
    optimization_eligibility: (
        GoalOptimizationEligibilityEnum.GoalOptimizationEligibility
    )
    retention_goal_settings: GoalSetting.RetentionGoal
    new_customer_acquisition_goal_settings: GoalSetting.NewCustomerAcquisitionGoal
    loyalty_retention_goal_settings: GoalSetting.LoyaltyRetentionGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        goal_id: int = ...,
        goal_type: GoalTypeEnum.GoalType = ...,
        owner_customer: str = ...,
        optimization_eligibility: GoalOptimizationEligibilityEnum.GoalOptimizationEligibility = ...,
        retention_goal_settings: GoalSetting.RetentionGoal = ...,
        new_customer_acquisition_goal_settings: GoalSetting.NewCustomerAcquisitionGoal = ...,
        loyalty_retention_goal_settings: GoalSetting.LoyaltyRetentionGoal = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "goal_id",
            "goal_type",
            "owner_customer",
            "optimization_eligibility",
            "retention_goal_settings",
            "new_customer_acquisition_goal_settings",
            "loyalty_retention_goal_settings",
        ],
    ) -> bool: ...
