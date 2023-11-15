from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v14.resources.types.customer_conversion_goal import (
    CustomerConversionGoal,
)

_M = TypeVar("_M")

class CustomerConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerConversionGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: CustomerConversionGoal = ...
    ) -> None: ...

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerConversionGoalOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomerConversionGoalOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCustomerConversionGoalResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomerConversionGoalResult] = ...
    ) -> None: ...
