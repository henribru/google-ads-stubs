from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.resources.types.custom_conversion_goal import CustomConversionGoal
from google.ads.googleads.v22.resources.types.custom_conversion_goal import CustomConversionGoal
from google.ads.googleads.v22.resources.types.custom_conversion_goal import CustomConversionGoal
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomConversionGoal
    update: CustomConversionGoal
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: CustomConversionGoal = ..., update: CustomConversionGoal = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateCustomConversionGoalResult(proto.Message):
    resource_name: str
    custom_conversion_goal: CustomConversionGoal
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., custom_conversion_goal: CustomConversionGoal = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "custom_conversion_goal"]) -> bool: ...
class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomConversionGoalOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CustomConversionGoalOperation] = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "validate_only", "response_content_type"]) -> bool: ...
class MutateCustomConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCustomConversionGoalResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateCustomConversionGoalResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results"]) -> bool: ...
