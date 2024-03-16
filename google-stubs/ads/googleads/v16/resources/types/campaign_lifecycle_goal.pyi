from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)
from google.ads.googleads.v16.enums.types.customer_acquisition_optimization_mode import (
    CustomerAcquisitionOptimizationModeEnum,
)

_M = TypeVar("_M")

class CampaignLifecycleGoal(proto.Message):
    resource_name: str
    campaign: str
    customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["resource_name", "campaign", "customer_acquisition_goal_settings"],
    ) -> bool: ...

class CustomerAcquisitionGoalSettings(proto.Message):
    optimization_mode: (
        CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    )
    value_settings: LifecycleGoalValueSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode = ...,
        value_settings: LifecycleGoalValueSettings = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["optimization_mode", "value_settings"]
    ) -> bool: ...
