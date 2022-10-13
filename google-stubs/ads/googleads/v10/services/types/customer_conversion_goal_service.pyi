from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.customer_conversion_goal import (
    CustomerConversionGoal,
)

class CustomerConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerConversionGoal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CustomerConversionGoal = ...
    ) -> None: ...

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerConversionGoalOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerConversionGoalOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: list[MutateCustomerConversionGoalResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomerConversionGoalResult] = ...
    ) -> None: ...
