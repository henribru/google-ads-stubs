from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)

_M = TypeVar("_M")

class CustomerLifecycleGoal(proto.Message):
    resource_name: str
    customer_acquisition_goal_value_settings: LifecycleGoalValueSettings
    owner_customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        customer_acquisition_goal_value_settings: LifecycleGoalValueSettings = ...,
        owner_customer: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "customer_acquisition_goal_value_settings",
            "owner_customer",
        ],
    ) -> bool: ...
