from google.ads.googleads.v18.common.types.lifecycle_goals import LifecycleGoalValueSettings
from google.ads.googleads.v18.enums.types.customer_acquisition_optimization_mode import CustomerAcquisitionOptimizationModeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignLifecycleGoal(proto.Message):
    resource_name: str
    campaign: str
    customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign: str = ..., customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "customer_acquisition_goal_settings"]) -> bool: ...
class CustomerAcquisitionGoalSettings(proto.Message):
    optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    value_settings: LifecycleGoalValueSettings
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, optimization_mode: CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode = ..., value_settings: LifecycleGoalValueSettings = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["optimization_mode", "value_settings"]) -> bool: ...
