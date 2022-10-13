from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.conversion_action import ConversionAction

class ConversionActionOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionAction
    update: ConversionAction
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ConversionAction = ...,
        update: ConversionAction = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionActionResult(proto.Message):
    resource_name: str
    conversion_action: ConversionAction
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        conversion_action: ConversionAction = ...
    ) -> None: ...

class MutateConversionActionsRequest(proto.Message):
    customer_id: str
    operations: list[ConversionActionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ConversionActionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionActionsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateConversionActionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateConversionActionResult] = ...
    ) -> None: ...
