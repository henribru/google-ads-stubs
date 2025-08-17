from google.ads.googleads.v20.common.types.lifecycle_goals import LifecycleGoalValueSettings
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerLifecycleGoal(proto.Message):
    resource_name: str
    customer_acquisition_goal_value_settings: LifecycleGoalValueSettings
    owner_customer: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., customer_acquisition_goal_value_settings: LifecycleGoalValueSettings = ..., owner_customer: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "customer_acquisition_goal_value_settings", "owner_customer"]) -> bool: ...
