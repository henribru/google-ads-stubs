from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.conversion_custom_variable import (
    ConversionCustomVariable,
)

_M = TypeVar("_M")

class ConversionCustomVariableOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionCustomVariable
    update: ConversionCustomVariable
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ConversionCustomVariable = ...,
        update: ConversionCustomVariable = ...
    ) -> None: ...

class MutateConversionCustomVariableResult(proto.Message):
    resource_name: str
    conversion_custom_variable: ConversionCustomVariable
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_custom_variable: ConversionCustomVariable = ...
    ) -> None: ...

class MutateConversionCustomVariablesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionCustomVariableOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionCustomVariableOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionCustomVariablesResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateConversionCustomVariableResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateConversionCustomVariableResult] = ...
    ) -> None: ...
