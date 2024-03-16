from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v16.resources.types.customer_lifecycle_goal import (
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
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation", "validate_only"]
    ) -> bool: ...

class ConfigureCustomerLifecycleGoalsResponse(proto.Message):
    result: ConfigureCustomerLifecycleGoalsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: ConfigureCustomerLifecycleGoalsResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...

class ConfigureCustomerLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...

class CustomerLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerLifecycleGoal
    update: CustomerLifecycleGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomerLifecycleGoal = ...,
        update: CustomerLifecycleGoal = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update"]
    ) -> bool: ...
