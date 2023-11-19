from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v13.resources.types.customer_conversion_goal import (
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
    def __contains__(self, key: Literal["update_mask", "update"]) -> bool: ...  # type: ignore[override]

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["customer_id", "operations", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCustomerConversionGoalResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomerConversionGoalResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results"]) -> bool: ...  # type: ignore[override]
