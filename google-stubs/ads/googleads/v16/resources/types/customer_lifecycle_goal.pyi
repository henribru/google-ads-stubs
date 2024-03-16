from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)

_M = TypeVar("_M")

class CustomerLifecycleGoal(proto.Message):
    class LifecycleGoalCustomerDefinitionSettings(proto.Message):
        existing_user_lists: MutableSequence[str]
        high_lifetime_value_user_lists: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            existing_user_lists: MutableSequence[str] = ...,
            high_lifetime_value_user_lists: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["existing_user_lists", "high_lifetime_value_user_lists"]
        ) -> bool: ...

    resource_name: str
    lifecycle_goal_customer_definition_settings: (
        CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings
    )
    customer_acquisition_goal_value_settings: LifecycleGoalValueSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        lifecycle_goal_customer_definition_settings: CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings = ...,
        customer_acquisition_goal_value_settings: LifecycleGoalValueSettings = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "lifecycle_goal_customer_definition_settings",
            "customer_acquisition_goal_value_settings",
        ],
    ) -> bool: ...
