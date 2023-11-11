from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v15.resources.types.customer_lifecycle_goal import (
    CustomerLifecycleGoal,
)

class ConfigureCustomerLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CustomerLifecycleGoalOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerLifecycleGoalOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class ConfigureCustomerLifecycleGoalsResponse(proto.Message):
    result: ConfigureCustomerLifecycleGoalsResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: ConfigureCustomerLifecycleGoalsResult = ...
    ) -> None: ...

class ConfigureCustomerLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class CustomerLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerLifecycleGoal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerLifecycleGoal = ...
    ) -> None: ...
