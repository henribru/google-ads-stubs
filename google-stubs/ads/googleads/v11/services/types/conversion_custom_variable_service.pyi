from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.conversion_custom_variable import (
    ConversionCustomVariable,
)

class ConversionCustomVariableOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionCustomVariable
    update: ConversionCustomVariable
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ConversionCustomVariable = ...,
        update: ConversionCustomVariable = ...
    ) -> None: ...

class MutateConversionCustomVariableResult(proto.Message):
    resource_name: str
    conversion_custom_variable: ConversionCustomVariable
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        conversion_custom_variable: ConversionCustomVariable = ...
    ) -> None: ...

class MutateConversionCustomVariablesRequest(proto.Message):
    customer_id: str
    operations: list[ConversionCustomVariableOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ConversionCustomVariableOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionCustomVariablesResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateConversionCustomVariableResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateConversionCustomVariableResult] = ...
    ) -> None: ...
