from typing import Any

import proto

from google.ads.googleads.v15.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)
from google.ads.googleads.v15.enums.types.customer_acquisition_optimization_mode import (
    CustomerAcquisitionOptimizationModeEnum,
)

class CampaignLifecycleGoal(proto.Message):
    resource_name: str
    campaign: str
    customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings = ...
    ) -> None: ...

class CustomerAcquisitionGoalSettings(proto.Message):
    optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    value_settings: LifecycleGoalValueSettings
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode = ...,
        value_settings: LifecycleGoalValueSettings = ...
    ) -> None: ...
