from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v21.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v21.resources.types.conversion_custom_variable import ConversionCustomVariable
from google.ads.googleads.v21.resources.types.conversion_custom_variable import ConversionCustomVariable
from google.ads.googleads.v21.resources.types.conversion_custom_variable import ConversionCustomVariable
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionCustomVariableOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionCustomVariable
    update: ConversionCustomVariable
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: ConversionCustomVariable = ..., update: ConversionCustomVariable = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update"]) -> bool: ...
class MutateConversionCustomVariableResult(proto.Message):
    resource_name: str
    conversion_custom_variable: ConversionCustomVariable
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., conversion_custom_variable: ConversionCustomVariable = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "conversion_custom_variable"]) -> bool: ...
class MutateConversionCustomVariablesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionCustomVariableOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[ConversionCustomVariableOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateConversionCustomVariablesResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateConversionCustomVariableResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateConversionCustomVariableResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
