from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.customer_conversion_goal import CustomerConversionGoal
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerConversionGoal
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., update: CustomerConversionGoal = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "update"]) -> bool: ...
class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerConversionGoalOperation]
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[CustomerConversionGoalOperation] = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "validate_only"]) -> bool: ...
class MutateCustomerConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCustomerConversionGoalResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., results: MutableSequence[MutateCustomerConversionGoalResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results"]) -> bool: ...
