from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

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

class ConfigureCustomerLifecycleGoalsResponse(proto.Message):
    result: ConfigureCustomerLifecycleGoalsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: ConfigureCustomerLifecycleGoalsResult = ...
    ) -> None: ...

class ConfigureCustomerLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

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
