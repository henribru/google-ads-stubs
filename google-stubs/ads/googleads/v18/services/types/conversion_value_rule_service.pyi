from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.conversion_value_rule import ConversionValueRule
from google.ads.googleads.v18.resources.types.conversion_value_rule import ConversionValueRule
from google.ads.googleads.v18.resources.types.conversion_value_rule import ConversionValueRule
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionValueRuleOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionValueRule
    update: ConversionValueRule
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: ConversionValueRule = ..., update: ConversionValueRule = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateConversionValueRuleResult(proto.Message):
    resource_name: str
    conversion_value_rule: ConversionValueRule
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., conversion_value_rule: ConversionValueRule = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "conversion_value_rule"]) -> bool: ...
class MutateConversionValueRulesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionValueRuleOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[ConversionValueRuleOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateConversionValueRulesResponse(proto.Message):
    results: MutableSequence[MutateConversionValueRuleResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateConversionValueRuleResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
