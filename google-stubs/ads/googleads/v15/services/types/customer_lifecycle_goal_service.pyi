from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v15.resources.types.customer_lifecycle_goal import (
    CustomerLifecycleGoal,
)

_M = TypeVar("_M")

class ConfigureCustomerLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CustomerLifecycleGoalOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerLifecycleGoalOperation = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operation", "validate_only"]) -> bool: ...  # type: ignore[override]

class ConfigureCustomerLifecycleGoalsResponse(proto.Message):
    result: ConfigureCustomerLifecycleGoalsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: ConfigureCustomerLifecycleGoalsResult = ...
    ) -> None: ...
    def __contains__(self, key: Literal["result"]) -> bool: ...  # type: ignore[override]

class ConfigureCustomerLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class CustomerLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerLifecycleGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomerLifecycleGoal = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "create"]) -> bool: ...  # type: ignore[override]
