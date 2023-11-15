from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)
from google.ads.googleads.v15.enums.types.customer_acquisition_optimization_mode import (
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
        customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings = ...
    ) -> None: ...

class CustomerAcquisitionGoalSettings(proto.Message):
    optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    value_settings: LifecycleGoalValueSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode = ...,
        value_settings: LifecycleGoalValueSettings = ...
    ) -> None: ...
