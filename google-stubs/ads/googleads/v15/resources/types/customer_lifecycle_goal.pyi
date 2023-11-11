from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.common.types.lifecycle_goals import (
    LifecycleGoalValueSettings,
)

class CustomerLifecycleGoal(proto.Message):
    class LifecycleGoalCustomerDefinitionSettings(proto.Message):
        existing_user_lists: MutableSequence[str]
        high_lifetime_value_user_lists: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            existing_user_lists: MutableSequence[str] = ...,
            high_lifetime_value_user_lists: MutableSequence[str] = ...
        ) -> None: ...
    resource_name: str
    lifecycle_goal_customer_definition_settings: CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings
    customer_acquisition_goal_value_settings: LifecycleGoalValueSettings
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        lifecycle_goal_customer_definition_settings: CustomerLifecycleGoal.LifecycleGoalCustomerDefinitionSettings = ...,
        customer_acquisition_goal_value_settings: LifecycleGoalValueSettings = ...
    ) -> None: ...
